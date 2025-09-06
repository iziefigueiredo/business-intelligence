import pandas as pd
from pathlib import Path

# Função para renomear colunas do csv PIB
def rename_select(df: pd.DataFrame) -> pd.DataFrame:
     df_final = df[[
        "V",
        "D1N",
        "D1C",
        "D2C"
    ]].rename(columns={
        "V": "pib",
        "D1N": "municipio",
        "D1C": "cod_mun",
        "D2C": "ano",
    })
     return df_final


def clean_columns(df: pd.DataFrame, columns: str) -> pd.DataFrame:
    df[columns] = df[columns].str.split('-').str[0].str.strip()
    return df

pasta_raw = Path("data/raw/")
arquivo_raw = pasta_raw / "pib_municipios.csv"
df_pib = pd.read_csv(arquivo_raw)

# Renomeia as colunas
df_pib_renomeado = rename_select(df_pib)
df_pib_renomeado = clean_columns(df_pib_renomeado, "municipio")

# Define a pasta e o caminho do arquivo processado
pasta_interim = Path("data/interim/")
pasta_interim.mkdir(parents=True, exist_ok=True)
arquivo_interim = pasta_interim / "pib_municipios.csv"

# Salva o DataFrame processado
df_pib_renomeado.to_csv(arquivo_interim, index=False)

print(f"O arquivo foi salvo com sucesso em: {arquivo_interim.resolve()}")