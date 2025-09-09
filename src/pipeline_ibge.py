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
from src.eda import profile_ibge as eda_ibge


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
    
    # Cria uma instância da classe IBGEProcessor
    processor = process_ibge.IBGEProcessor()
    
    # Chama o método de processamento e salvamento através da instância
    processor.process_save(
        input_file="pib_municipios.csv",
        output_file="pib_clean.csv",
        rename_map=processor.RENAME_MAP_PIB
    )
    processor.process_save(
        input_file="populacao_municipios.csv",
        output_file="populacao_clean.csv",
        rename_map=processor.RENAME_MAP_POPULATION
    )
    
    # Etapa 3: Unificação (Junta os dados de PIB e População)
    print("Executando a etapa de Unificação...")
    merge_ibge.unify_ibge()
    
    # Etapa 4: Análise Exploratória de Dados (EDA)
    print("Executando a etapa de Análise Exploratória de Dados (EDA)...")
    eda_ibge.profile_ibge()
    print("--- Pipeline do IBGE concluído com sucesso! ---")

if __name__ == "__main__":
    run_pipeline_ibge()