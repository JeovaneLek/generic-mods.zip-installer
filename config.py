from pathlib import Path
import json


def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    config["downloads_folder"] = Path(config["downloads_folder"])
    config["mods_folder"] = Path(config["mods_folder"])

    return config
