import os
import shutil
import struct

SOURCE = "entry.png"
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_png_size(path):
    """Return the (width, height) stored in a PNG file's IHDR chunk."""
    with open(path, "rb") as handle:
        signature = handle.read(8)
        if signature != PNG_SIGNATURE:
            return None
        chunk = handle.read(25)
        width, height = struct.unpack(">II", chunk[8:16])
        return width, height


def main():
    print("Starting entry build.")
    print("Source image: " + SOURCE)
    if not os.path.isdir(OUTPUT_DIR):
        print("Creating output directory: " + OUTPUT_DIR)
        os.makedirs(OUTPUT_DIR)
    print("Copying image to " + OUTPUT + " ...")
    shutil.copyfile(SOURCE, OUTPUT)
    print("Copy finished.")
    size = read_png_size(OUTPUT)
    if size is None:
        print("Warning: the output file is not a valid PNG image.")
    else:
        print("Image dimensions: %d x %d" % size)


if __name__ == "__main__":
    main()
