import pandas as pd
from pathlib import Path


def clean_columns(df: pd.DataFrame, rename_map: dict) -> pd.DataFrame:
    """
    Seleciona e renomeia colunas de um DataFrame com base em um dicionário de mapeamento.
    """
    colunas_desejadas = list(rename_map.keys())
    
    # Filtra as colunas que realmente existem no DataFrame
    cols_exist = [c for c in colunas_desejadas if c in df.columns]
    
    if not cols_exist:
        raise ValueError("Nenhuma das colunas desejadas foi encontrada.")
        
    # Seleciona as colunas existentes e as renomeia
    df_clean = df[cols_exist].rename(columns=rename_map)
    return df_clean


def limpar_municipio(df: pd.DataFrame, coluna: str) -> pd.DataFrame:
    """
    Remove a sigla do estado e espaços em branco extras do nome do município.
    """
    df[coluna] = df[coluna].str.split('-').str[0].str.strip()
    return df


def processar_salvar(
    arquivo_entrada: str, 
    arquivo_saida: str, 
    renome_map: dict
):
    """
    Processa e salva um arquivo CSV, usando as funções de limpeza.
    """
    dir_entrada = Path("data/raw/")
    dir_entrada.mkdir(parents=True, exist_ok=True)

    dir_saida = Path("data/interim/")
    dir_saida.mkdir(parents=True, exist_ok=True)

    arquivo_entrada_path = dir_entrada / arquivo_entrada
    arquivo_saida_path = dir_saida / arquivo_saida
    
    try:
        tabela = pd.read_csv(arquivo_entrada_path, encoding="utf-8")
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {arquivo_entrada_path}")
        return

    #  Renomeia as colunas
    df_renomeado = clean_columns(tabela, renome_map)
    
    #  Limpa o nome do município
    df_final = limpar_municipio(df_renomeado, "municipio")

    #  Salva o resultado final
    df_final.to_csv(arquivo_saida_path, index=False, encoding="utf-8")
    
    print(f"Salvo: {arquivo_saida_path} | Linhas: {len(df_final)} | Colunas: {list(df_final.columns)}")


# ===== Mapeamento de colunas para cada fonte de dados =====
RENOME_MAP_PIB = {      
    "V":   "pib",
    "D1N": "municipio",
    "D1C": "cod_mun",
    "D2C": "ano",
}

RENOME_MAP_POPULACAO = {     
    "V":   "populacao",
    "D1N": "municipio",
    "D1C": "cod_mun",
    "D2C": "ano",
}

# ===== Execução principal =====
if __name__ == "__main__":
    processar_salvar(
        arquivo_entrada="pib_municipios.csv",
        arquivo_saida="pib_limpo.csv",
        renome_map=RENOME_MAP_PIB
    )

    processar_salvar(
        arquivo_entrada="populacao_municipios.csv",
        arquivo_saida="populacao_limpo.csv",
        renome_map=RENOME_MAP_POPULACAO
    )