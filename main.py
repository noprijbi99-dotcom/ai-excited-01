import os
import shutil
import struct

def main():
    source = 'entry.png'
    dest_dir = '/output'
    dest = os.path.join(dest_dir, 'entry.png')

    # Create /output if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Copy entry.png byte-for-byte
    print(f"Copying {source} to {dest}...")
    shutil.copy2(source, dest)
    print("Copy complete.")

    # Validation within the script (optional but good for debugging)
    with open(source, 'rb') as f:
        header = f.read(24)
        if header[:8] != b'\x89PNG\r\n\x1a\n':
            print("Warning: Not a valid PNG file header.")
        else:
            # PNG dimensions are at offset 16 (4 bytes for width, 4 bytes for height)
            width, height = struct.unpack('>II', header[16:24])
            print(f"Dimensions: {width}x{height}")

if __name__ == "__main__":
    main()
