# src/pipeline_sim.py

import sys
from pathlib import Path

# Adiciona a raiz do projeto ao caminho de importação
# Isso é crucial para que o script encontre os módulos, não importa onde ele seja executado
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

# Importa as funções de cada etapa do pipeline
from src.extract import sim as extract_sim
from src.merge import unify_sim 
from src.transform import processing_sim

def run_pipeline_sim():
    """
    Orquestra o pipeline completo do SIM, de ponta a ponta.
    """
    print("--- Iniciando o Pipeline do SIM ---")

    # Etapa 1: Extração (Download dos arquivos brutos)
    print("Executando a etapa de Extração...")
    extract_sim.run()
    
    # Etapa 2: Unificação (Junta os arquivos baixados)
    print("Executando a etapa de Unificação...")
    unify_sim.unify_sim()
    
    # Etapa 3: Processamento (Limpeza e tratamento)
    print("Executando a etapa de Processamento...")
    processing_sim.processed_sim()
    
    print("--- Pipeline do SIM concluído com sucesso! ---")


if __name__ == "__main__":
    run_pipeline_sim()