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
    

    def accident_type(self, df):
        """Classify accident type based on CAUSABAS."""
        if df.empty:
            return pd.DataFrame()

        # Create a new column with default value
        df['TIPO_ACIDENTE'] = 'Outras causas'
      
         # Pedestre: V01-V09
        df.loc[df['CAUSABAS'].str.match(r'V0[1-9]', na=False), 'TIPO_ACIDENTE'] = 'Pedestre'
        # Ciclista: V10-V19
        df.loc[df['CAUSABAS'].str.match(r'V1[0-9]', na=False), 'TIPO_ACIDENTE'] = 'Ciclista'
        # Motociclista: V20-V29
        df.loc[df['CAUSABAS'].str.match(r'V2[0-9]', na=False), 'TIPO_ACIDENTE'] = 'Motociclista'
        # Ocupante de automóvel: V40-V49
        df.loc[df['CAUSABAS'].str.match(r'V4[0-9]', na=False), 'TIPO_ACIDENTE'] = 'Ocupante de automovel'
        # Ocupante de caminhonete: V50-V59
        df.loc[df['CAUSABAS'].str.match(r'V5[0-9]', na=False), 'TIPO_ACIDENTE'] = 'Ocupante de caminhonete'
        # Ocupante de veiculo de transporte pesado: V60-V69
        df.loc[df['CAUSABAS'].str.match(r'V6[0-9]', na=False), 'TIPO_ACIDENTE'] = 'Ocupante de veiculo de transporte pesado'
        # Ocupante de onibus: V70-V79
        df.loc[df['CAUSABAS'].str.match(r'V7[0-9]', na=False), 'TIPO_ACIDENTE'] = 'Ocupante de onibus'
        # Outros acidentes de transporte terrestre: V80-V89
        df.loc[df['CAUSABAS'].str.match(r'V8[0-9]', na=False), 'TIPO_ACIDENTE'] = 'Outros acidentes de transporte terrestre'
        # Acidentes de transporte por agua, aereo, espacial e outros nao especificados: V90-V99
        df.loc[df['CAUSABAS'].str.match(r'V9[0-9]', na=False), 'TIPO_ACIDENTE'] = 'Outros'
        
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
        df = self.accident_type(df)
        self.save(df)
        return df

def run():
    processor = SIMProcessor()
    processor.run()

if __name__ == "__main__":
    run()