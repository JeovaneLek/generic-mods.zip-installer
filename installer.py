import json
import shutil
import zipfile
from pathlib import Path


def carregar_config():
    with open("config.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados


config = carregar_config()
downloads = Path(config["downloads_folder"])
print("Procurando arquivos .zip...\n")

encontrou_zip = False
contador = 1

mods = []

for arquivo in downloads.iterdir():

    if arquivo.suffix == ".zip":
        encontrou_zip = True

        print(f"{contador} - {arquivo.name}")

        contador += 1

if not encontrou_zip:
    print("Nenhum arquivo .zip foi encontrado.")


def encontrar_zips():
    pass


def instalar_mod():
    pass


def instalar_todos():
    pass


def main():
    pass
