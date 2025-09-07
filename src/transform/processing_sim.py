import pandas as pd
from pathlib import Path

def processed_sim():
    """
    Carrega, seleciona colunas e salva os dados do SIM.
    """
    # Define o arquivo de entrada e de saída
    dir_entrada = Path("data/interim/")
    dir_saida = Path("data/processed/")
    
    arquivo_entrada = dir_entrada / "sim_unified.csv"
    arquivo_saida = dir_saida / "sim.csv"

    # Garante que os diretórios de saída existem
    dir_saida.mkdir(parents=True, exist_ok=True)

    # Lista das colunas que você quer manter
    colunas_desejadas = [
        "DTOBITO", "HORAOBITO", "CAUSABAS", "DTNASC", "SEXO", "IDADE", "RACACOR", "ESC",
        "CODMUNRES", "CODMUNOCOR"
    ]

    # Carrega o arquivo unificado
    try:
        tabela = pd.read_csv(arquivo_entrada, low_memory=False)
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {arquivo_entrada}")
        return

    # Seleciona apenas as colunas desejadas que existem na tabela
    colunas_existentes = [c for c in colunas_desejadas if c in tabela.columns]
    tabela_final = tabela[colunas_existentes]

    # Salva o resultado final com a seleção de colunas
    tabela_final.to_csv(arquivo_saida, index=False, encoding="utf-8")

    print(f"Dados filtrados salvos em: {arquivo_saida.resolve()}")
    print(f"Colunas salvas: {colunas_existentes}")

if __name__ == "__main__":
    processed_sim()