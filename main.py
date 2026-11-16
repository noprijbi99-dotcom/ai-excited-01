"""Paper Plane to the Judge — entry runner.

Copies the entry image (entry.png) byte-for-byte to /output/entry.png
and prints the image dimensions read from the PNG header.
Standard library only.
"""

import os
import shutil
import struct

SOURCE = "entry.png"
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def read_png_size(path):
    """Return (width, height) from a PNG file header."""
    with open(path, "rb") as handle:
        header = handle.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file: bad signature")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
        print("Created output directory: " + DEST_DIR)
    if not os.path.exists(SOURCE):
        raise FileNotFoundError("entry image missing: " + SOURCE)
    print("Copying " + SOURCE + " to " + DEST + " ...")
    shutil.copy2(SOURCE, DEST)
    print("Copy finished.")
    width, height = read_png_size(SOURCE)
    print("Dimensions: " + str(width) + "x" + str(height))


if __name__ == "__main__":
    main()
