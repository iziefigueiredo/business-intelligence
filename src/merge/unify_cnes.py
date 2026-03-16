import pandas as pd
from pathlib import Path

COLUNAS = ["CNES", "CODUFMUN", "QTLEITP1", "QTLEITP2", "QTLEITP3"]

def unify_cnes(pasta_entrada: str = "data/raw/cnes/", pasta_saida: str = "data/interim/"):
    """
    Unifica todos os arquivos parquet do CNES, seleciona colunas e salva.
    """
    dir_entrada = Path(pasta_entrada)
    dir_saida = Path(pasta_saida)
    dir_saida.mkdir(parents=True, exist_ok=True)

    arquivos = list(dir_entrada.rglob("*.parquet"))

    if not arquivos:
        print(f"Nenhum arquivo .parquet encontrado em {dir_entrada}.")
        return None

    tabelas = [pd.read_parquet(arq, columns=COLUNAS) for arq in arquivos]
    tabela_unificada = pd.concat(tabelas, ignore_index=True)

    caminho_saida = dir_saida / "cnes_unified.csv"
    tabela_unificada.to_csv(caminho_saida, index=False, encoding="utf-8")

    print(f"Arquivo unificado salvo em: {caminho_saida.resolve()}")
    print(f"Shape: {tabela_unificada.shape}")
    print(f"Colunas: {tabela_unificada.columns.tolist()}")

    return tabela_unificada

if __name__ == "__main__":
    unify_cnes()