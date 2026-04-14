from pysus.online_data.SIM import SIM
from pathlib import Path

def run():
    pasta = Path("data/raw/sim/")
    pasta.mkdir(parents=True, exist_ok=True)

    sim = SIM().load()

    arquivos = sim.get_files("CID10", uf="RS", year=2022)
    sim.download(arquivos, local_dir=pasta)

    print("Download concluído!")

if __name__ == "__main__":
    run()