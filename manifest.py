from pathlib import Path
import json
import zipfile


def read_manifest_from_zip(zip_path: Path) -> dict | None:
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_file:
            for file_name in zip_file.namelist():
                if Path(file_name).name.lower() == "manifest.json":
                    with zip_file.open(file_name) as file:
                        return json.load(file)

    except (zipfile.BadZipFile, json.JSONDecodeError):
        return None

    return None


def read_manifest_from_folder(mod_folder: Path) -> dict | None:
    manifest_path = mod_folder / "manifest.json"

    if not manifest_path.is_file():
        return None

    try:
        with manifest_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return None


def is_mod_installed(zip_path: Path, mods_path: Path) -> bool:
    zip_manifest = read_manifest_from_zip(zip_path)

    if zip_manifest is None or "UniqueID" not in zip_manifest:
        return False

    for mod_folder in mods_path.iterdir():

        if not mod_folder.is_dir():
            continue

        folder_manifest = read_manifest_from_folder(mod_folder)

        if folder_manifest is None:
            continue

        if folder_manifest.get("UniqueID") == zip_manifest["UniqueID"]:
            return True

    return False
