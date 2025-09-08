import pandas as pd
from pathlib import Path

class SIMProcessor:
    """
    Class to process SIM data.
    """

    def __init__(self, in_dir="data/interim/", out_dir="data/processed/"):
        self.in_dir = Path(in_dir)
        self.out_dir = Path(out_dir)
        self.in_file = self.in_dir / "sim_unified.csv"
        self.out_file = self.out_dir / "sim.csv"

        # Columns to keep
        self.keep_cols = [
            "DTOBITO", "HORAOBITO", "CAUSABAS", "DTNASC", "SEXO",
            "IDADE", "RACACOR", "ESC", "CODMUNRES", "CODMUNOCOR"
        ]

        # Ensure output dir exists
        self.out_dir.mkdir(parents=True, exist_ok=True)

    def load(self):
        """Load SIM CSV."""
        try:
            df = pd.read_csv(self.in_file, low_memory=False)
            print(f"Loaded file: {self.in_file.resolve()}")
            return df
        except FileNotFoundError:
            print(f"Error: file not found → {self.in_file}")
            return None

    def filter(self, df):
        """Filter only existing keep_cols."""
        cols = [c for c in self.keep_cols if c in df.columns]
        df_final = df[cols]
        print(f"Cols kept: {cols}")
        return df_final

    def save(self, df):
        """Save processed CSV."""
        df.to_csv(self.out_file, index=False, encoding="utf-8")
        print(f"Saved file: {self.out_file.resolve()}")

    def run(self):
        """Run full pipeline."""
        df = self.load()
        if df is None:
            return None
        df_final = self.filter(df)
        self.save(df_final)
        return df_final


if __name__ == "__main__":
    sim = SIMProcessor()
    sim.run()
