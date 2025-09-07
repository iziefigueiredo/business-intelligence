import pandas as pd
from pathlib import Path

def unify_ibge():
    """
    Carrega os dados de PIB e População processados, unifica-os
    e calcula o PIB per capita.
    """
    print("--- Unificando dados de IBGE ---")

    # Carregar os DataFrames da pasta interim
    dir_interim = Path("data/interim/")
    pib_df = pd.read_csv(dir_interim / "pib_clean.csv")
    populacao_df = pd.read_csv(dir_interim / "populacao_clean.csv")

    # Unificar os DataFrames
    # A união é feita pela coluna 'cod_mun'
    df_unificado = pd.merge(pib_df, populacao_df, on="cod_mun", how="inner", suffixes=("_pib", "_pop"))

    # Remover as colunas duplicadas
    df_unificado.drop(columns=["municipio_pop", "ano_pop"], inplace=True)

    # Renomear as colunas unificadas
    df_unificado.rename(columns={"municipio_pib": "municipio", "ano_pib": "ano"}, inplace=True)
    
  
    # Salvar o resultado final na pasta 'processed'
    dir_processed = Path("data/processed/")
    dir_processed.mkdir(parents=True, exist_ok=True)
    df_unificado.to_csv(dir_processed / "ibge.csv", index=False)
    print(f"\nArquivo final salvo em: {dir_processed / 'ibge.csv'}")

    return df_unificado


if __name__ == "__main__":
    unify_ibge()