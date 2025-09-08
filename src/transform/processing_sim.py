import pandas as pd
from pathlib import Path

class SIMProcessor:
    """Process SIM data."""

    def __init__(self, in_dir="data/interim/", out_dir="data/processed/"):
        self.in_dir = Path(in_dir)
        self.out_dir = Path(out_dir)
        self.in_file = self.in_dir / "sim_unified.csv"
        self.out_file = self.out_dir / "sim.csv"
        
        self.keep_cols_map = {
            "DTOBITO": "DTOBITO",
            "HORAOBITO": "HORAOBITO",
            "CAUSABAS": "CAUSABAS",
            "DTNASC": "DTNASC",
            "SEXO": "SEXO",
            "IDADE": "IDADE",
            "RACACOR": "RACACOR",
            "ESC": "ESC",
            "CODMUNRES": "CODMUNRES",
            "CODMUNOCOR": "CODMUNOCOR"
        }
        self.out_dir.mkdir(parents=True, exist_ok=True)

    def load(self):
        try:
            df = pd.read_csv(self.in_file, low_memory=False)
            print(f"Loaded: {self.in_file.resolve()}")
            return df
        except FileNotFoundError:
            print(f"Error: file not found → {self.in_file}. Check if the unification step has been executed.")
            return pd.DataFrame()

    def filter(self, df):
        """Maps and selects the desired columns."""
        if df.empty:
            return pd.DataFrame()
        
        df_filtered = df.rename(columns=self.keep_cols_map)
        
        cols = [c for c in self.keep_cols_map.values() if c in df_filtered.columns]
        
        if not cols:
            print("Warning: None of the desired columns were found.")
        
        df_final = df_filtered.loc[:, cols].copy()
        print(f"Columns kept: {cols}")
        return df_final
        
    def convert_date(self, df):
        """DTOBITO and DTNASC -> dd/mm/yy from YYYYMMDD."""
        if df.empty:
            return pd.DataFrame()
        
        for col in ["DTOBITO", "DTNASC"]:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], format="%Y%m%d", errors="coerce").dt.strftime("%d/%m/%y")
        return df

    def convert_time(self, df):
        """HORAOBITO -> HH:MM from HHMM."""
        if df.empty:
            return pd.DataFrame()

        if "HORAOBITO" in df.columns:
            df["HORAOBITO"] = df["HORAOBITO"].astype(str).str.strip().str.extract(r"(\d{1,4})")[0].fillna("")
            df["HORAOBITO"] = df["HORAOBITO"].str.zfill(4)
            df["HORAOBITO"] = pd.to_datetime(df["HORAOBITO"], format="%H%M", errors="coerce").dt.strftime("%H:%M")
        return df

    def save(self, df):
        if df.empty:
            print("Warning: Empty DataFrame. No file saved.")
            return
            
        self.out_file.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(self.out_file, index=False, encoding="utf-8")
        print(f"Saved: {self.out_file.resolve()}") 
   
    def run(self):
        df = self.load()
        if df.empty:
            print("Error: No data loaded. The processing step cannot be completed.")
            return
        
        df = self.filter(df)
        df = self.convert_date(df)
        df = self.convert_time(df)
        
        self.save(df)
        return df

def run():
    processor = SIMProcessor()
    processor.run()

if __name__ == "__main__":
    run()