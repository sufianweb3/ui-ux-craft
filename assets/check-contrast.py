#!/usr/bin/env python3
"""Verify the documented text/border contrast pairs in tokens.css.

OKLCH -> OKLab -> linear sRGB (clipped to gamut, as browsers render) -> WCAG 2.2 relative luminance.
Usage: python3 check-contrast.py [path/to/tokens.css]
Exit code 1 if any pair is below its threshold.
"""
import math, re, sys

path = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("check-contrast.py", "tokens.css")
css = re.sub(r"/\*.*?\*/", "", open(path, encoding="utf-8").read(), flags=re.S)

def block(selector_regex, nth=0):
    """Return {--name: value} for the nth rule whose selector matches selector_regex."""
    hits = [m for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css) if re.search(selector_regex, m.group(1).strip())]
    body = hits[nth].group(2)
    return {k.strip(): v.strip() for k, v in re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", body)}

prim = block(r"^:root$", 0)                                   # primitives
light = {**prim, **block(r"^:root, \[data-theme=\"light\"\]$", 0)}
dark = {**prim, **block(r"^\[data-theme=\"dark\"\]$", 0)}
light_ic = {**light, **block(r"^:root, \[data-theme=\"light\"\]$", 1)}
dark_ic = {**dark, **block(r"^\[data-theme=\"dark\"\]$", 1)}

def resolve(v, ctx, depth=0):
    while "var(" in v and depth < 20:
        v = re.sub(r"var\((--[\w-]+)\)", lambda m: ctx[m.group(1)], v); depth += 1
    return v

def oklch_to_lin(L, C, H):
    a, b = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s3 = l_ ** 3, m_ ** 3, s_ ** 3
    r = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s3
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s3
    bl = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s3
    return [r, g, bl]

def in_gamut(lin):
    return all(-1e-4 <= c <= 1 + 1e-4 for c in lin)

def encode(lin):
    lin = [min(1, max(0, c)) for c in lin]
    return [12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055 for c in lin]

def oklch_to_srgb(s):
    """Return ([clipped sRGB, chroma-reduced sRGB], out_of_gamut). Browsers differ (clip vs CSS Color 4
    gamut mapping), so ratios are checked against both renderings and the worse one is reported."""
    L, C, H = [float(x) for x in re.match(r"oklch\(\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)", s).groups()]
    lin = oklch_to_lin(L, C, H)
    if in_gamut(lin):
        return [encode(lin)], False
    lo, hi = 0.0, C
    for _ in range(40):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if in_gamut(oklch_to_lin(L, mid, H)) else (lo, mid)
    return [encode(lin), encode(oklch_to_lin(L, lo, H))], True

def lum(rgb):
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]

def color(token, ctx):
    v = resolve(ctx[token] if token.startswith("--") else token, ctx)
    return oklch_to_srgb(v)

def ratio(fg, bg, ctx):
    (fs, fo), (bs, bo) = color(fg, ctx), color(bg, ctx)
    worst = min((max(lum(f), lum(b)) + 0.05) / (min(lum(f), lum(b)) + 0.05) for f in fs for b in bs)
    return worst, fo or bo

T, U = 4.5, 3.0   # text, UI boundary (WCAG 1.4.3 / 1.4.11)
pairs = {
  "light": (light, [
    ("--color-text-primary", "--p-gray-0", T), ("--color-text-primary", "--p-gray-50", T),
    ("--color-text-secondary", "--p-gray-0", T), ("--color-text-secondary", "--p-gray-100", T),
    ("--color-text-tertiary", "--p-gray-0", T), ("--color-text-tertiary", "--p-gray-100", T), ("--color-text-tertiary", "--p-gray-150", T),
    ("--color-text-on-accent", "--color-accent", T), ("--color-text-on-accent", "--color-accent-hover", T),
    ("--color-text-on-danger", "--color-danger", T),
    ("--color-text-link", "--p-gray-0", T), ("--color-text-link", "--p-gray-100", T),
    ("--color-text-primary", "--color-bg-selected", T),
    ("--color-border-control", "--p-gray-0", U), ("--color-border-control", "--p-gray-50", U), ("--color-border-control", "--p-gray-100", U),
    ("--color-focus-ring", "--p-gray-0", U), ("--color-focus-ring", "--p-gray-50", U),
    ("--color-danger", "--p-gray-0", T), ("--color-danger", "--color-danger-subtle", T),
    ("--color-success", "--p-gray-0", T), ("--color-success", "--color-success-subtle", T),
    ("--color-warning", "--p-gray-0", T), ("--color-warning", "--color-warning-subtle", T),
    ("--color-info", "--p-gray-0", T), ("--color-info", "--color-info-subtle", T),
  ]),
  "dark": (dark, [
    ("--color-text-primary", "--p-gray-950", T), ("--color-text-primary", "--p-gray-1000", T),
    ("--color-text-secondary", "--p-gray-950", T), ("--color-text-secondary", "--p-gray-900", T),
    ("--color-text-tertiary", "--p-gray-950", T), ("--color-text-tertiary", "--p-gray-900", T), ("--color-text-tertiary", "--p-gray-850", T),
    ("--color-text-on-accent", "--color-accent", T), ("--color-text-on-accent", "--color-accent-hover", T),
    ("--color-text-on-danger", "--color-danger", T),
    ("--color-text-link", "--p-gray-950", T), ("--color-text-link", "--p-gray-900", T),
    ("--color-text-primary", "--color-bg-selected", T),
    ("--color-border-control", "--p-gray-950", U), ("--color-border-control", "--p-gray-1000", U), ("--color-border-control", "--p-gray-900", U),
    ("--color-focus-ring", "--p-gray-950", U), ("--color-focus-ring", "--p-gray-1000", U),
    ("--color-danger", "--p-gray-950", T), ("--color-danger", "--color-danger-subtle", T),
    ("--color-success", "--p-gray-950", T), ("--color-success", "--color-success-subtle", T),
    ("--color-warning", "--p-gray-950", T), ("--color-warning", "--color-warning-subtle", T),
    ("--color-info", "--p-gray-950", T), ("--color-info", "--color-info-subtle", T),
  ]),
  "light + increased contrast": (light_ic, [
    ("--color-text-primary", "--p-gray-0", T), ("--color-text-secondary", "--p-gray-0", T), ("--color-text-secondary", "--p-gray-100", T),
    ("--color-text-tertiary", "--p-gray-0", T), ("--color-text-tertiary", "--p-gray-100", T),
    ("--color-text-link", "--p-gray-0", T), ("--color-text-on-accent", "--color-accent", T), ("--color-text-on-accent", "--color-accent-hover", T),
    ("--color-text-on-danger", "--color-danger", T),
    ("--color-border-subtle", "--p-gray-0", U), ("--color-border-control", "--p-gray-0", U), ("--color-focus-ring", "--p-gray-0", U),
    ("--color-danger", "--p-gray-0", T), ("--color-success", "--p-gray-0", T), ("--color-warning", "--p-gray-0", T), ("--color-info", "--p-gray-0", T),
    ("--color-danger", "--color-danger-subtle", T), ("--color-success", "--color-success-subtle", T),
    ("--color-warning", "--color-warning-subtle", T), ("--color-info", "--color-info-subtle", T),
  ]),
  "dark + increased contrast": (dark_ic, [
    ("--color-text-primary", "--p-gray-950", T), ("--color-text-secondary", "--p-gray-950", T),
    ("--color-text-tertiary", "--p-gray-950", T), ("--color-text-tertiary", "--p-gray-900", T),
    ("--color-text-link", "--p-gray-950", T), ("--color-text-on-accent", "--color-accent", T), ("--color-text-on-accent", "--color-accent-hover", T),
    ("--color-text-on-danger", "--color-danger", T),
    ("--color-border-subtle", "--p-gray-950", U), ("--color-border-control", "--p-gray-950", U), ("--color-focus-ring", "--p-gray-950", U),
    ("--color-danger", "--p-gray-950", T), ("--color-success", "--p-gray-950", T), ("--color-warning", "--p-gray-950", T), ("--color-info", "--p-gray-950", T),
    ("--color-danger", "--color-danger-subtle", T), ("--color-success", "--color-success-subtle", T),
    ("--color-warning", "--color-warning-subtle", T), ("--color-info", "--color-info-subtle", T),
  ]),
}

fails = 0
for mode, (ctx, rows) in pairs.items():
    print(f"\n## {mode}")
    for fg, bg, need in rows:
        r, oog = ratio(fg, bg, ctx)
        ok = r >= need
        fails += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {math.floor(r*10)/10:5.1f}:1 (exact {r:.3f}, need {need})  {fg} on {bg}{'  [out of sRGB gamut: worse of clip / chroma-reduce]' if oog else ''}")
print(f"\n{fails} failing pair(s)")
sys.exit(1 if fails else 0)
