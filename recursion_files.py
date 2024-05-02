import os
import shutil

def copy_files(source_dir, destination_dir):
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isdir(item_path):
            copy_files(item_path, destination_dir)  # Рекурсивно викликаємо функцію для піддиректорії
        else:
            shutil.copy(item_path, destination_dir)  # Копіюємо файл у директорію призначення

def main():
    source_dir = input("Enter the source directory: ")
    destination_dir = input("Enter the destination directory: ")

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    copy_files(source_dir, destination_dir)

if __name__ == "__main__":
    main()
