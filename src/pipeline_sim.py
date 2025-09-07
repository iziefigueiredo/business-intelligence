# pipeline_sim.py

import pandas as pd
from pathlib import Path

# --- Importações ---
from extract import sim as extract_sim
from merge import unify_sim as unify_sim
from transform import processing_sim as process_sim

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
    process_sim.processar_sim()
    
    print("--- Pipeline do SIM concluído com sucesso! ---")


if __name__ == "__main__":
    run_pipeline_sim()