
# merge/unify.py
import pandas as pd
from pathlib import Path

def unify_sim(pasta_entrada: str = "data/raw/", pasta_saida: str = "data/interim"):
    """
    Unifica todos os arquivos parquet do SIM em um único DataFrame e o salva.
    """
    # Define o caminho da pasta de entrada e de saída
    dir_entrada = Path(pasta_entrada)
    dir_saida = Path(pasta_saida)

    # Garante que o diretório de saída existe
    dir_saida.mkdir(parents=True, exist_ok=True)

    # Lista todos os arquivos parquet na pasta de entrada
    arquivos = list(dir_entrada.rglob("*.parquet"))
    
    if not arquivos:
        print(f"Nenhum arquivo .parquet encontrado em {dir_entrada}.")
        return None

    # Carrega e concatena todos os DataFrames
    tabelas = [pd.read_parquet(arq) for arq in arquivos]
    tabela_unificada = pd.concat(tabelas, ignore_index=True)

    # Salva o DataFrame unificado
    caminho_saida = dir_saida / "sim_unified.csv"
    tabela_unificada.to_csv(caminho_saida, index=False, encoding ="utf-8")

    print(f"Arquivo unificado salvo em: {caminho_saida.resolve()}")
    print(f"Linhas: {len(tabela_unificada)}")
    
    return tabela_unificada

# Este bloco só é executado se você rodar o script diretamente
if __name__ == "__main__":
    df_sim = unify_sim()