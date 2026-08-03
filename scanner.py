from pathlib import Path


def find_zips(downloads_path: Path) -> list[Path]:

    mods = []

    for file in downloads_path.iterdir():
        if file.suffix.lower() == ".zip":
            mods.append(file)


    return mods
