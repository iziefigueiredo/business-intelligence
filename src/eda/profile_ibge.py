
# src/profile_ibge.py

import pandas as pd
from pathlib import Path
from ydata_profiling import ProfileReport

def profile_ibge():
    """
    Carrega o DataFrame unificado do IBGE e gera um relatório de perfil de dados.
    """
    print("--- Gerando o perfil de dados do IBGE ---")

    # Path setup
    processed_dir = Path("data/processed/")
    docs_dir = Path("docs/")
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    input_file = processed_dir / "ibge.csv"
    output_file = docs_dir / "ibge_profile.html"
    
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {input_file}")
        print("Certifique-se de que o pipeline do IBGE foi executado.")
        return

    # Gera o relatório de perfil
    profile = ProfileReport(df, title="Relatório de Perfil de Dados do IBGE")

    # Salva o relatório como um arquivo HTML
    profile.to_file(output_file)
    
    print(f"Relatório de perfil de dados salvo em: {output_file.resolve()}")


if __name__ == "__main__":
    profile_ibge()