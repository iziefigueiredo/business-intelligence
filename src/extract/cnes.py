from pysus.online_data.CNES import CNES
from pathlib import Path

def run():
    pasta = Path("data/raw/cnes/")
    pasta.mkdir(parents=True, exist_ok=True)

    cnes = CNES().load()
    arquivos = cnes.get_files("ST", uf="RS", year=2022)
    baixados = cnes.download(arquivos, local_dir=pasta)

    print(f"{len(baixados)} arquivos baixados com sucesso!")

if __name__ == "__main__":
    run()