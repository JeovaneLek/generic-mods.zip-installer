import json
import shutil
import zipfile
from pathlib import Path


def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def find_zips(downloads_path):
    print("Searching for .zip files...\n")

    mods = []

    for file in downloads_path.iterdir():
        if file.suffix == ".zip":
            mods.append(file)

    if not mods:
        print("No .zip files found.")
        return mods

    for index, file in enumerate(mods, start=1):
        print(f"{index} - {file.name}")

    return mods


def install_mod():
    pass


def install_all():
    pass


def main():
    config = load_config()

    downloads_path = Path(config["downloads_folder"])

    mods = find_zips(downloads_path)

    print(f"\nFound {len(mods)} mod(s).")


if __name__ == "__main__":
    main()
