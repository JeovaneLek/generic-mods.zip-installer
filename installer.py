from pathlib import Path
import zipfile


def install_mod(mod: Path, mods_path: Path) -> bool:
    try:
        with zipfile.ZipFile(mod, "r") as zip_file:
            zip_file.extractall(mods_path)

        mod.unlink()

        print(f'"{mod.name}" installed successfully!')
        return True

    except zipfile.BadZipFile:
        print(f'"{mod.name}" is not a valid ZIP file.')

    except OSError as error:
        print(f'Could not install "{mod.name}": {error}')

    return False


def install_all_mods(mods: list[Path], mods_path: Path) -> int:
    installed = 0

    for mod in mods:
        if install_mod(mod, mods_path):
            installed += 1

    return installed
