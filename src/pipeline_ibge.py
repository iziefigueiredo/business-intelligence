# src/pipeline_ibge.py

import sys
from pathlib import Path

# Adiciona a raiz do projeto ao caminho de importação
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

# Importa as funções de cada etapa do pipeline
from src.extract import ibge as extract_ibge
from src.transform import processing_ibge as process_ibge
from src.merge import unify_ibge as merge_ibge


def run_pipeline_ibge():
    """
    Orquestra o pipeline completo dos dados do IBGE, de ponta a ponta.
    """
    print("--- Iniciando o Pipeline do IBGE ---")

    # Etapa 1: Extração (Download dos arquivos brutos)
    print("Executando a etapa de Extração...")
    extract_ibge.run()
    
    # Etapa 2: Processamento (Limpeza e tratamento)
    print("Executando a etapa de Processamento...")
    # Chama as funções para processar e salvar os dados de PIB e População separadamente
    process_ibge.processar_salvar(
        arquivo_entrada="pib_municipios.csv",
        arquivo_saida="pib_clean.csv",
        renome_map=process_ibge.RENOME_MAP_PIB
    )
    process_ibge.processar_salvar(
        arquivo_entrada="populacao_municipios.csv",
        arquivo_saida="populacao_clean.csv",
        renome_map=process_ibge.RENOME_MAP_POPULACAO
    )
    
    # Etapa 3: Unificação (Junta os dados de PIB e População)
    print("Executando a etapa de Unificação...")
    merge_ibge.unify_ibge()
    
    print("--- Pipeline do IBGE concluído com sucesso! ---")


if __name__ == "__main__":
    run_pipeline_ibge()