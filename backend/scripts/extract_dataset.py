import zipfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET_FOLDER = PROJECT_ROOT / "datasets" / "ODIR"

ZIP_FILE = DATASET_FOLDER / "archive (1).zip"

EXTRACT_FOLDER = DATASET_FOLDER / "images"


def extract_dataset():

    if not ZIP_FILE.exists():
        print(f"[ERROR] ZIP file not found:\n{ZIP_FILE}")
        return

    EXTRACT_FOLDER.mkdir(exist_ok=True)

    if any(EXTRACT_FOLDER.iterdir()):
        print("[INFO] Dataset already extracted.")
        return

    print("[INFO] Extracting dataset...")

    with zipfile.ZipFile(ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(EXTRACT_FOLDER)

    print("[SUCCESS] Dataset extracted successfully.")


if __name__ == "__main__":
    extract_dataset()