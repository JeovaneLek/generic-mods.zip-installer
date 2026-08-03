from pathlib import Path
import zipfile


def install_mod(mod, mods_path: Path) -> None:
    try:
        with zipfile.ZipFile(mod, "r") as zip_file:
            zip_file.extractall(mods_path)

        print(f'"{mod.name}" installed successfully!')

    except zipfile.BadZipFile as error:
        print(f"Error: {error}")
    
