import pandas as pd
from pathlib import Path

RENAME_MAP = {
    "CODUFMUN": "cod_municipio",
    "QTLEITP1": "leitos_cirurgicos",
    "QTLEITP2": "leitos_clinicos",
    "QTLEITP3": "leitos_complementares",
}

class CNESProcessor:
    def __init__(self, in_dir="data/interim/", out_dir="data/processed/"):
        self.in_file = Path(in_dir) / "cnes_unified.csv"
        self.out_file = Path(out_dir) / "cnes.csv"
        Path(out_dir).mkdir(parents=True, exist_ok=True)

    def load(self):
        df = pd.read_csv(self.in_file, low_memory=False)
        print(f"Carregado: {df.shape}")
        return df

    def process(self, df):
        # Renomear colunas
        df = df.rename(columns=RENAME_MAP)

        # Converter leitos para numérico
        for col in ["leitos_cirurgicos", "leitos_clinicos", "leitos_complementares"]:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

        # Calcular total de leitos por estabelecimento
        df["total_leitos"] = df["leitos_cirurgicos"] + df["leitos_clinicos"] + df["leitos_complementares"]

        # Agrupar por município
        df = df.groupby("cod_municipio", as_index=False).agg(
            qtd_estabelecimentos=("CNES", "count"),
            total_leitos=("total_leitos", "sum")
        )

        print(f"Processado: {df.shape}")
        return df

    def save(self, df):
        df.to_csv(self.out_file, index=False, encoding="utf-8")
        print(f"Salvo em: {self.out_file.resolve()}")

    def run(self):
        df = self.load()
        df = self.process(df)
        self.save(df)
        return df

if __name__ == "__main__":
    CNESProcessor().run()