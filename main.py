from pathlib import Path
import shutil
from ai_classifier import classify_file, CATEGORIES

FOLDER_TO_ORGANIZE = Path("files_to_organize")
ORGANIZED_FOLDER = Path("organized_files")
ORGANIZED_FOLDER.mkdir(exist_ok=True)

def organize_files(dry_run=True):
    files = [f for f in FOLDER_TO_ORGANIZE.iterdir() if f.is_file()]
    for file in files:
        category = classify_file(file)
        target_dir = ORGANIZED_FOLDER / category
        target_dir.mkdir(exist_ok=True)

        if dry_run:
            print(f"[DRY RUN] Would move {file.name} -> {category}/")
        else:
            shutil.move(str(file), target_dir / file.name)
            print(f"Moved {file.name} -> {category}/")

if __name__ == "__main__":
    print("Starting AI File Organizer...")
    organize_files(dry_run=False)  # Dry run disabled — actually move files
    print("Done!")
