from pysus import SIM
from pathlib import Path

# Inicializa o SIM
sim = SIM().load()

# Define a pasta de destino
pasta = Path("data/raw/")
pasta.mkdir(parents=True, exist_ok=True)

# Define os anos 
anos = list(range(2018,2021 ))  


arquivos_baixar = []

# Busca os arquivos para cada ano e mês
for ano in anos:
    arquivos = sim.get_files("CID10", uf="RS", year=ano)
    arquivos_baixar.extend(arquivos)

# Faz o download de todos os arquivos para a pasta

baixados = sim.download(arquivos_baixar, local_dir=pasta)

print(f"{len(baixados)} arquivos baixados com sucesso!")