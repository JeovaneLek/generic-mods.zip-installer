import os

from installer import install_all_mods, install_mod
from manifest import is_mod_installed
from scanner import find_zips


TITLE = "Zip Mod Installer"


def clear_terminal() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def show_menu() -> None:
    print(f"""
        {TITLE}

        [1] Install one mod
        [2] Install all mods
        [0] Exit
        """)


def show_mods(mods: list) -> None:
    print("\nAvailable mods:\n")

    for index, mod in enumerate(mods, start=1):
        print(f"{index} - {mod.name}")

    print("\n0 - Back")


def ask_confirmation(prompt: str) -> str:
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("y", "n"):
            return answer

        print("Invalid option. Please enter y or n.")


def main_menu(config: dict) -> None:
    downloads_path = config["downloads_folder"]
    mods_path = config["mods_folder"]

    while True:

        clear_terminal()
        show_menu()

        try:
            option = int(input("\nChoose an option: "))

        except ValueError:
            clear_terminal()
            print("Invalid input.")
            input("\nPress Enter to continue...")
            continue

        # Clear the previous menu before opening the selected option.
        clear_terminal()

        match option:

            case 1:
                mods = find_zips(downloads_path)

                if not mods:
                    print("No .zip files found.")
                    input("\nPress Enter to continue...")
                    continue

                while True:

                    show_mods(mods)

                    try:
                        choice = int(input("\nChoose a mod: "))

                    except ValueError:
                        clear_terminal()
                        print("Invalid input.")
                        continue

                    # Return to the main menu.
                    if choice == 0:
                        break

                    # Validate the selected mod.
                    if not 1 <= choice <= len(mods):
                        clear_terminal()
                        print("Invalid option.")
                        continue

                    selected_mod = mods[choice - 1]

                    # Check whether the mod is already installed.
                    if is_mod_installed(selected_mod, mods_path):

                        print("\nThis mod is already installed.")

                        confirm = ask_confirmation(
                            "\nDo you want to reinstall it? (y/n): "
                        )

                        if confirm == "n":
                            continue

                    clear_terminal()

                    if install_mod(selected_mod, mods_path):
                        print(
                            f'Mod "{selected_mod.name}" '
                            "installed successfully!"
                        )
                    else:
                        print(
                            f'Failed to install "{selected_mod.name}".'
                        )

                    input("\nPress Enter to continue...")
                    break

            case 2:
                mods = find_zips(downloads_path)

                if not mods:
                    print("No .zip files found.")
                    input("\nPress Enter to continue...")
                    continue

                mods_to_install = []
                already_installed = []

                print("Checking installed mods...\n")

                for mod in mods:

                    if is_mod_installed(mod, mods_path):
                        already_installed.append(mod)

                    else:
                        mods_to_install.append(mod)

                # Handle already installed mods.
                if already_installed:

                    print(
                        "The following mods are already installed:\n"
                    )

                    for mod in already_installed:
                        print(f"- {mod.name}")

                    confirm = ask_confirmation(
                        "\nDo you want to reinstall them? (y/n): "
                    )

                    if confirm == "y":
                        mods_to_install.extend(already_installed)

                    else:
                        print(
                            "\nAlready installed mods will be skipped."
                        )

                # Nothing remains to install.
                if not mods_to_install:
                    print("\nNo mods to install.")
                    input("\nPress Enter to continue...")
                    continue

                clear_terminal()

                print("The following mods will be installed:\n")

                for mod in mods_to_install:
                    print(f"- {mod.name}")

                confirm = ask_confirmation(
                    "\nDo you want to install these mods? (y/n): "
                )

                if confirm == "n":
                    print("\nInstallation cancelled.")
                    input("\nPress Enter to continue...")
                    continue

                clear_terminal()

                installed = install_all_mods(
                    mods_to_install,
                    mods_path
                )

                skipped = len(mods) - len(mods_to_install)
                failed = len(mods_to_install) - installed

                print("\nInstallation complete!")
                print(f"Installed: {installed}")
                print(f"Skipped: {skipped}")
                print(f"Failed: {failed}")

                input("\nPress Enter to continue...")

            case 0:
                print("Exiting...")
                break

            case _:
                print("Choose a valid option.")
                input("\nPress Enter to continue...")
