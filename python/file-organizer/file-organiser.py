import os
import shutil
import time

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".js", ".sh", ".bat"]
}

SCRIPT_NAME = os.path.basename(__file__)

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    summary = {}

    for folder in FILE_TYPES:
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)
        summary[folder] = 0

    os.makedirs(os.path.join(folder_path, "Others"), exist_ok=True)
    summary["Others"] = 0

    for file in os.listdir(folder_path):

        if file == SCRIPT_NAME:
            continue

        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                destination = os.path.join(folder_path, folder)
                shutil.move(file_path, os.path.join(destination, file))
                summary[folder] += 1
                print(f"Moved: {file} --> {folder}")
                moved = True
                break

        if not moved:
            destination = os.path.join(folder_path, "Others")
            shutil.move(file_path, os.path.join(destination, file))
            summary["Others"] += 1
            print(f"Moved: {file} --> Others")

    print("\n" + "=" * 45)
    print("          ORGANIZATION SUMMARY")
    print("=" * 45)

    total = 0
    for folder, count in summary.items():
        print(f"{folder:<12}: {count}")
        total += count

    print("-" * 45)
    print(f"Total Files : {total}")
    print("=" * 45)
    print("Folder organized successfully!")

def main():
    print("=" * 45)
    print("          FILE ORGANIZER")
    print("=" * 45)
    print("Loading...")
    time.sleep(1)

    choice = input("Use current folder? (yes/no): ").strip().lower()

    if choice == "yes":
        folder = os.getcwd()
    else:
        folder = input("Enter folder path: ").strip()

    print("\nOrganizing files...")
    time.sleep(1)

    organize_folder(folder)

    print("\nThank you for using File Organizer!")
    time.sleep(1)

if __name__ == "__main__":
    main()