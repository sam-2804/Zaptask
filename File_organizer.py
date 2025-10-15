import os
from pathlib import Path
import shutil

def master(dir_to_organize):                 
    folders = ["Images", "Documents", "Misc", "Videos", "Compressed", "Music"]

    extension_map = {
        "Documents": [".xlsx", ".pdf", ".py"],
        "Images": [".png", ".jpg", ".webp"],
        "Videos": [".mp4"],
        "Compressed": [".zip", ".7z"],
        "Music": [".mp3"]
    }

    base_path = Path(dir_to_organize)
    files_in_folder = os.listdir(base_path)

    # Create missing folders 
    for folder in folders:
        folder_path = base_path / folder
        folder_path.mkdir(exist_ok=True)

    # Organize files
    for file in files_in_folder:
        file_path = base_path / file
        if file_path.is_dir():
            continue  # Skip folders

        file_extension = file_path.suffix.lower()
        moved = False
        for folder, ext_list in extension_map.items():
            if file_extension in ext_list:
                shutil.move(str(file_path), str(base_path / folder / file))
                moved = True
                break
        if not moved:
            shutil.move(str(file_path), str(base_path / "Misc" / file))


if __name__ == "__main__":
    print("you executed File_organizer.py")
else:
    print("you imported this file from somewhere else")