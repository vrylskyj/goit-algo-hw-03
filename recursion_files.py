import os
import shutil
import sys

def copy_files(source_dir, destination_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1].strip('.')
            destination_path = os.path.join(destination_dir, extension)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            try:
                shutil.copy(source_path, destination_path)
                print(f"File '{file}' copied to '{destination_path}'")
            except IOError as e:
                print(f"Unable to copy file '{file}': {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [<destination_directory>]")
        sys.exit(1)

    source_dir = sys.argv[1]
    destination_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        sys.exit(1)

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    copy_files(source_dir, destination_dir)

if __name__ == "__main__":
    main()
