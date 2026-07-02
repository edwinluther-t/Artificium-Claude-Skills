"""Capture phase-stepped frames of an ANIMATED flow template and stitch a looping
GIF with PIL. No ffmpeg required. Temp-only; not committed.

Works for any template that uses the shared animated-dot mechanism:
  - a live `<body ...>` (or bare `<body>`) tag with NO data-phase, and
  - CSS rules `body[data-phase="0".."5"] ... .dot{left:...}` that freeze the dots.

Usage:
  python make_flow_gif.py [OUT.gif] [TEMPLATE] [W] [H]
    OUT.gif   output path            (default: $TEMP/flow.gif)
    TEMPLATE  template stem or file  (default: animated-flow-map)
              e.g. "layered-loop-map" or a full .html path
    W H       canvas size            (defaults per template below)

Examples:
  python make_flow_gif.py out.gif animated-flow-map           # 1080x1500
  python make_flow_gif.py out.gif layered-loop-map 1080 1400
"""
import os, re, subprocess, tempfile, pathlib, sys
from PIL import Image

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TPLDIR = pathlib.Path(__file__).parent / "templates"

# default canvas per template (keep in sync with each template's --w/--h)
SIZES = {"animated-flow-map": (1080, 1500), "layered-loop-map": (1080, 1400)}

OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(tempfile.gettempdir()) / "flow.gif"
TPL = sys.argv[2] if len(sys.argv) > 2 else "animated-flow-map"
SRC = (pathlib.Path(TPL) if TPL.endswith(".html") else (TPLDIR / f"{TPL}.html")).resolve()
stem = SRC.stem
W = int(sys.argv[3]) if len(sys.argv) > 3 else SIZES.get(stem, (1080, 1500))[0]
H = int(sys.argv[4]) if len(sys.argv) > 4 else SIZES.get(stem, (1080, 1500))[1]
STEPS = 6
SCALE = 1  # GIF: keep 1x to bound file size (2x retina would be ~4x bytes)

base = SRC.read_text(encoding="utf-8")
# exact-tag swap on the REAL <body> tag (matches bare <body> OR <body ...attrs>,
# but NOT the head comment or CSS `body[data-phase=...]` selectors — those have no
# leading `<`). Strip any existing data-phase, then inject data-phase="{k}".
BODY_RE = re.compile(r'<body\b[^>]*>')
m = BODY_RE.search(base)
if not m:
    raise SystemExit(f"no <body> tag found in {SRC}")
body_open = m.group(0)
body_noPhase = re.sub(r'\s*data-phase="[^"]*"', '', body_open)

tmpdir = pathlib.Path(tempfile.mkdtemp(prefix="flowgif_"))
frames = []
for k in range(STEPS):
    tag = body_noPhase[:-1] + f' data-phase="{k}">'
    html = base.replace(body_open, tag, 1)
    fp = tmpdir / f"frame_{k}.html"
    fp.write_text(html, encoding="utf-8")
    png = tmpdir / f"frame_{k}.png"
    udd = tmpdir / f"udd_{k}"
    uri = fp.resolve().as_uri()
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
        f"--user-data-dir={udd}", f"--force-device-scale-factor={SCALE}",
        f"--window-size={W},{H}", "--hide-scrollbars", "--virtual-time-budget=4000",
        f"--screenshot={png}", uri], check=True,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    img = Image.open(png).convert("RGB")
    frames.append(img)
    print(f"frame {k}: {png} {img.size}")

frames[0].save(OUT, save_all=True, append_images=frames[1:],
    duration=140, loop=0, optimize=False, disposal=2)
print(f"GIF: {OUT} ({os.path.getsize(OUT)} bytes, {STEPS} frames, {stem})")
