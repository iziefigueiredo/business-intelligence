import pandas as pd
from pathlib import Path
from ydata_profiling import ProfileReport

def profile_cnes():
    print("--- Gerando o perfil de dados do CNES ---")

    processed_dir = Path("data/processed/")
    docs_dir = Path("reports/")
    docs_dir.mkdir(parents=True, exist_ok=True)

    input_file = processed_dir / "cnes.csv"
    output_file = docs_dir / "cnes_profile.html"

    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {input_file}")
        return

    profile = ProfileReport(df, title="Relatório de Perfil de Dados do CNES")
    profile.to_file(output_file)

    print(f"Relatório salvo em: {output_file.resolve()}")

if __name__ == "__main__":
    profile_cnes()