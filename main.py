from config import load_config
from menu import main_menu

def main():
    config = load_config()
    main_menu(config)


if __name__ == "__main__":
   main()
