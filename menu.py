from scanner import find_zips
from installer import install_mod

TITLE = "Zip Mod Installer"

def show_menu():

    print(f"""
          {TITLE}

        [1] Install one mod
        [2] Install all mods
        [0] Exit
        """)

def show_mods(mods):
    print("\nAvailable mods:\n")

    for index, mod in enumerate(mods, start=1):
        print(f"{index} - {mod.name}")

    print("\n0 - Back")

def main_menu(config):

    downloads_path = config["downloads_folder"]
    mods_path = config["mods_folder"]

    while True:  # Main menu

        show_menu()

        option = int(input("\nChoose an option: "))

        if 

        match option:
            case 1:
                mods = find_zips(downloads_path)

                if not mods:
                    print("No .zip files found.")
                    break

                while True:  # Mod selection menu

                    show_mods(mods)

                    try:
                        choice = int(input("Choose a mod: "))

                    except ValueError:
                        print("Invalid input.")
                        continue

                    # Want to exit this menu?
                    if choice == 0:
                        break

                    # Valid choice?
                    if 1 <= choice <= len(mods):
                        selected_mod = mods[choice - 1]
                        install_mod(selected_mod, mods_path)
                        print(f"Mod {selected_mod.name} successfully installed!")
                        break
                    else:
                        print("Invalid option")

            case 2:
                print("\nNot implemented yet.")

            case 0:
                print("Exiting...")
                break

            case _:
                print("\nChoose a valid option.")

