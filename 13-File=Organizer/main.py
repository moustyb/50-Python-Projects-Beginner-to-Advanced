# main.py
import os
import shutil

def organize_files(folder):
    if not os.path.exists(folder):
        print("Folder does not exist.")
        return

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        ext = filename.split(".")[-1].lower()
        if not ext:
            ext = "others"

        # Create target folder
        target_folder = os.path.join(folder, ext)
        os.makedirs(target_folder, exist_ok=True)

        # Move file
        shutil.move(file_path, os.path.join(target_folder, filename))
        print(f"Moved: {filename} → {ext}/")

def main():
    print("📂 File Organizer")
    folder = input("Enter folder path to organize: ").strip()
    organize_files(folder)
    print("Organization complete!")

if __name__ == "__main__":
    main()
