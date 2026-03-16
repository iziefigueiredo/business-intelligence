import sys
from pathlib import Path

project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from src.extract import cnes as extract_cnes
from src.merge import unify_cnes
from src.transform.preprocessing_cnes import CNESProcessor
from src.eda import profile_cnes as eda_cnes

def run_pipeline_cnes():
    print("--- Iniciando o Pipeline do CNES ---")

    print("Executando a etapa de Extração...")
    extract_cnes.run()

    print("Executando a etapa de Unificação...")
    unify_cnes.unify_cnes()

    print("Executando a etapa de Processamento...")
    CNESProcessor().run()

    print("Executando a etapa de Análise Exploratória de Dados (EDA)...")
    eda_cnes.profile_cnes()

    print("--- Pipeline do CNES concluído com sucesso! ---")

if __name__ == "__main__":
    run_pipeline_cnes()