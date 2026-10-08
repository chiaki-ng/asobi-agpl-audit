"""Render selected, reproducible IPA-byte excerpts as public PNG exhibits.

Install Pillow, then pass four independently obtained matching analysis IPAs.
The PNGs are rendered excerpts of archive contents, not app UI screenshots.
"""
import argparse
import hashlib
from pathlib import Path
import plistlib
import re
import textwrap
import zipfile

from PIL import Image, ImageDraw, ImageFont

EXPECTED = {
    "1.1.8": "e55276988c7964f4973feed85f568ffa69836408556dbf36a5f2a7a6d12bcf68",
    "1.1.9": "c4e26ea624d358934cda93fbbba082d925428677c7a0cd5470336b58b4939001",
    "1.3": "88f4a3dfa01be2401a566723540f1c742d02369bf78a4ddf05705fd09d4a931c",
    "1.3.1": "e68c6cf102dee10fe58caa550025af5387a8b7387a2b25cdfb417541a9c29b26",
}
APP = "Payload/AsobiMobile.app/"
NOTES = ("ADD_TO_XCODE.md", "IMPLEMENTATION_SUMMARY.md", "README.md",
         "TAKION_FIXES.md", "UI_INTEGRATION.md")
FONT = "/System/Library/Fonts/Menlo.ttc"
WIDTH = 1700
FG = "#e6edf3"
MUTED = "#93a4b6"
ACCENT = "#74c7ec"
BG = "#0d1117"
BOX = "#161b22"


def font(size):
    return ImageFont.truetype(FONT, size)


def load(path, version):
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED[version]:
        raise ValueError(f"{version}: unexpected IPA SHA-256 {digest}")
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        info = plistlib.loads(archive.read(APP + "Info.plist"))
        if info["CFBundleShortVersionString"] != version:
            raise ValueError(f"{version}: Info.plist version mismatch")
        note = archive.read(APP + "IMPLEMENTATION_SUMMARY.md").decode("utf-8").splitlines() if APP + "IMPLEMENTATION_SUMMARY.md" in names else []
        fixes = archive.read(APP + "TAKION_FIXES.md").decode("utf-8").splitlines() if APP + "TAKION_FIXES.md" in names else []
        executable = archive.read(APP + "AsobiMobile")
        strings = {m.decode("latin-1").strip() for m in re.findall(rb"[\x20-\x7e]{12,}", executable)}
        return {"version": version, "hash": digest, "names": names, "note": note,
                "fixes": fixes, "strings": strings}


def render(path, title, source, hash_lines, rows, foot):
    wrapped = [(label, textwrap.wrap(value, width=90, break_long_words=False)) for label, value in rows]
    height = 170 + sum(62 + 30 * (len(lines) - 1) for _, lines in wrapped) + 65 + 28 * len(hash_lines)
    image = Image.new("RGB", (WIDTH, height), BG)
    draw = ImageDraw.Draw(image)
    draw.text((54, 38), title, font=font(34), fill=FG)
    draw.text((54, 92), source, font=font(21), fill=ACCENT)
    y = 145
    for label, lines in wrapped:
        block = 54 + 30 * (len(lines) - 1)
        draw.rounded_rectangle((40, y - 7, WIDTH - 40, y + block - 7), radius=10, fill=BOX)
        draw.text((58, y), label, font=font(20), fill=MUTED)
        for offset, line in enumerate(lines):
            draw.text((450, y + 30 * offset), line, font=font(20), fill=FG)
        y += block + 8
    y += 8
    draw.text((54, y), foot, font=font(19), fill=ACCENT)
    y += 35
    for line in hash_lines:
        draw.text((54, y), line, font=font(18), fill=MUTED)
        y += 27
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, format="PNG", optimize=True)


def pick(strings, exact):
    matches = [s for s in strings if s == exact]
    if len(matches) != 1:
        raise ValueError(f"Missing exact executable string: {exact}")
    return matches[0]


def main():
    parser = argparse.ArgumentParser()
    for v in EXPECTED:
        parser.add_argument("--ipa-" + v.replace(".", "-"), type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    d = {v: load(getattr(args, "ipa_" + v.replace(".", "_")), v) for v in EXPECTED}
    a, b, c, e = (d[v] for v in EXPECTED)
    render(args.out / "01-bundled-chiaki-note.png",
           "1 · Developer note inside Asobi 1.1.8 IPA",
           APP + "IMPLEMENTATION_SUMMARY.md / TAKION_FIXES.md",
           ["IPA SHA-256 " + a["hash"]],
           [("SUMMARY:5", a["note"][4]),
            ("SUMMARY:44", a["note"][43]),
            ("SUMMARY:57", a["note"][56]),
            ("FIXES:1", a["fixes"][0])],
           "Verbatim selected lines; source member names and line numbers shown.")
    lines = (
        "Starting CTRL receive loop (Chiaki ctrl.c:307-490)...",
        "Step 4: DATA holepunch (Chiaki session.c:561-582)",
        "Step 4.5: SENKUSHA on DATA socket (Chiaki session.c:611-639)",
        "STEP 9: DATA ACCEPT exchange (Chiaki holepunch.c:1507-1556)",
    )
    render(args.out / "02-executable-source-citations.png",
           "2 · Source-range citations in Asobi 1.1.8",
           APP + "AsobiMobile · printable strings, whitespace trimmed",
           ["IPA SHA-256 " + a["hash"]],
           [(f"String {i}", pick(a["strings"], line)) for i, line in enumerate(lines, 1)],
           "Exact stored strings in the executable; no full binary is reproduced.")
    pairs = (
        (lines[0], "Starting CTRL receive loop..."),
        (lines[1], "Step 4: DATA holepunch"),
        (lines[3], "STEP 9: DATA ACCEPT exchange"),
    )
    rows = []
    for i, (before, after) in enumerate(pairs, 1):
        rows += [(f"{i} · 1.1.8", pick(a["strings"], before)),
                 (f"{i} · 1.1.9", pick(b["strings"], after))]
    render(args.out / "03-citation-removal.png",
           "3 · Citations removed in Asobi 1.1.9",
           APP + "AsobiMobile · paired exact executable strings",
           ["1.1.8 IPA SHA-256 " + a["hash"], "1.1.9 IPA SHA-256 " + b["hash"]],
           rows,
           "The 1.1.9 IPA still contains the five bundled Markdown notes.")
    if not all(APP + n in c["names"] for n in NOTES) or any(APP + n in e["names"] for n in NOTES):
        raise ValueError("Unexpected bundled-note presence")
    render(args.out / "04-bundled-notes-removed.png",
           "4 · Bundled notes disappear in Asobi 1.3.1",
           "ZIP member inventory from two IPAs · " + APP,
           ["1.3 IPA SHA-256 " + c["hash"], "1.3.1 IPA SHA-256 " + e["hash"]],
           [(name, "1.3: present    →    1.3.1: absent") for name in NOTES],
           "Five selected member names; this image does not show app runtime behavior.")


if __name__ == "__main__":
    main()
