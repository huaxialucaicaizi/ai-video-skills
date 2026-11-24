"""Pick the LXGW WenKai (OFL) webfont chunks that cover the characters used in some HTML files.

Usage: python3 lxgw_chunks.py <lxgw-wenkai-webfont package dir> <out dir> <file.html> [...]
Get the package with: npm pack lxgw-wenkai-webfont@1.7.0 && tar xzf lxgw-wenkai-webfont-1.7.0.tgz
Writes <out>/lxgw.css (bold weight, only needed @font-face blocks) + the chunk files + OFL.txt.
"""
import re, shutil, sys, pathlib

pkg, out, files = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3:]
text = "".join(pathlib.Path(f).read_text(encoding="utf-8") for f in files)
chars = {ord(c) for c in text if ord(c) >= 0x20}
css = (pkg / "lxgwwenkai-bold.css").read_text(encoding="utf-8")
out.mkdir(parents=True, exist_ok=True)
keep = []
for block in re.findall(r"@font-face\s*{[^}]*}", css):
    rng = re.search(r"unicode-range:\s*([^;}]*)", block).group(1)
    cps = set()
    for part in rng.split(","):
        a, _, b = part.strip()[2:].partition("-")
        cps.update(range(int(a, 16), int(b or a, 16) + 1))
    if chars & cps:
        src = re.search(r"url\('\./files/([^']+)'\)", block).group(1)
        shutil.copy(pkg / "files" / src, out / src)
        keep.append(block.replace("./files/", "./").replace("font-display: swap", "font-display: block"))
shutil.copy(pkg / "OFL.txt", out / "OFL.txt")
(out / "lxgw.css").write_text("/* LXGW WenKai Bold, SIL OFL 1.1 (see OFL.txt). Chunks from lxgw-wenkai-webfont (MIT). */\n" + "\n".join(keep) + "\n", encoding="utf-8")
print(f"{len(keep)} chunks for {len(chars)} chars")
