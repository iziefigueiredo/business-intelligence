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

    def _norm_cod(s: pd.Series) -> pd.Series:
        return (
            s.astype(str)
             .str.replace(r"\D", "", regex=True)
             .str.strip()
             .str.zfill(7)   # ajuste p/ 6 se a sua base usar 6 dígitos
        )

    pib_df["cod_mun"] = _norm_cod(pib_df["cod_mun"])
    populacao_df["cod_mun"] = _norm_cod(populacao_df["cod_mun"])

    
    # Unificar apenas a interseção real
    df_unified = pd.merge(
        pib_df,
        populacao_df,
        on="cod_mun",
        how="inner",
        suffixes=("_pib", "_pop")
    )

    # Remover colunas duplicadas se existirem
    drop_cols = [c for c in ["municipio_pop", "ano_pop"] if c in df_unified.columns]
    if drop_cols:
        df_unified.drop(columns=drop_cols, inplace=True)
    
    df_unified['pib']   = df_unified['pib'].astype(int)
    df_unified['populacao'] = df_unified['populacao'].astype(int)
    
    # Calcular PIB per capita
    df_unified["pib_per_capita"] = df_unified["pib"] / df_unified['populacao']

  
    # Salvar o resultado final na pasta 'processed'
    dir_processed = Path("data/processed/")
    dir_processed.mkdir(parents=True, exist_ok=True)
    df_unified.to_csv(dir_processed / "ibge.csv", index=False)
    print(f"\nArquivo final salvo em: {dir_processed / 'ibge.csv'}")

    return df_unified


if __name__ == "__main__":
    unify_ibge()