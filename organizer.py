import os
import shutil

def organize_files(folder_path):
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Music": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Programs": [".exe", ".msi", ".bat"],
        "Others": []
    }

    for folder in file_types.keys():
        folder_dir = os.path.join(folder_path, folder)
        os.makedirs(folder_dir, exist_ok=True)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder, extensions in file_types.items():
            if file_ext in extensions:
                dest_path = os.path.join(folder_path, folder, filename)
                shutil.move(file_path, dest_path)
                moved = True
                break

        if not moved:
            dest_path = os.path.join(folder_path, "Others", filename)
            shutil.move(file_path, dest_path)

    print("✅ Files organized successfully!")

if __name__ == "__main__":
    folder_to_organize = input("Enter the full path of the folder to organize: ").strip()

    if os.path.exists(folder_to_organize):
        organize_files(folder_to_organize)
    else:
        print("❌ The specified path does not exist. Please try again.")
