from pathlib import Path


def find_zips(downloads_path: Path) -> list[Path]:
    if not downloads_path.is_dir():
        return []

    return [
        file
        for file in downloads_path.iterdir()
        if file.is_file() and file.suffix.lower() == ".zip"
    ]
