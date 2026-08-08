# Zip Mod Installer

A lightweight command-line tool for installing Stardew Valley mods from ZIP files.

The project was created as a Python learning project focused on modular architecture, file handling, JSON parsing, and clean separation of responsibilities.

## Features

- Scan a Downloads folder for `.zip` mod files
- Install individual mods
- Install multiple mods at once
- Detect already installed mods
- Compare mods using their `UniqueID`
- Ask for confirmation before reinstalling mods
- Handle invalid ZIP files
- Cross-platform terminal clearing
- Configuration through JSON
- Type hints throughout the project
- Automatically remove ZIP files after successful installation

## Project Structure

ModInstaller/
├── main.py
├── config.py
├── scanner.py
├── manifest.py
├── installer.py
├── menu.py
├── config.example.json
├── .gitignore
└── README.md

## Configuration

The project uses a local `config.json` file to define the folders used by the installer.


   json
{
    "downloads_folder": "",
    "mods_folder": ""
    "delete_zip_after_install": true or false, you choose.
}

## Requirementes

- Python 3.10 or newer
- Valid mod directory

## Installation

git clone <repository-url>
cd ModInstaller

 Remember to edit config.json file!

## Usage

Just run: python mod_installer.py

## License

This project was created for educational purposes.
