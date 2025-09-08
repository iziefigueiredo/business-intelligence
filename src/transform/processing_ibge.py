import pandas as pd
from pathlib import Path

class IBGEProcessor:
    """Processes and saves IBGE data."""

    def __init__(self, in_dir="data/raw/", out_dir="data/interim/"):
        self.in_dir = Path(in_dir)
        self.out_dir = Path(out_dir)
        self.out_dir.mkdir(parents=True, exist_ok=True)

        self.RENAME_MAP_PIB = {      
            "V": "pib",
            "D1N": "municipio",
            "D1C": "cod_mun",
            "D2C": "ano",
        }

        self.RENAME_MAP_POPULATION = {     
            "V": "populacao",
            "D1N": "municipio",
            "D1C": "cod_mun",
            "D2C": "ano",
        }

    def clean_columns(self, df: pd.DataFrame, rename_map: dict) -> pd.DataFrame:
        """
        Selects and renames columns of a DataFrame based on a mapping dictionary.
        """
        desired_columns = list(rename_map.keys())
        existing_cols = [c for c in desired_columns if c in df.columns]
        
        if not existing_cols:
            raise ValueError("None of the desired columns were found.")
            
        df_clean = df[existing_cols].rename(columns=rename_map)
        return df_clean

    def clean_municipio(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        """
        Removes the state acronym and extra whitespace from the municipality name.
        """
        df[column] = df[column].str.split('-').str[0].str.strip()
        return df

 
        
        
    
    def process_and_save(self, input_file: str, output_file: str, rename_map: dict):
        """
        Loads, processes, and saves a CSV file.
        """
        input_path = self.in_dir / input_file
        output_path = self.out_dir / output_file
        
        try:
            table = pd.read_csv(input_path, encoding="utf-8")
        except FileNotFoundError:
            print(f"Error: File not found in {input_path}")
            return

        df_renamed = self.clean_columns(table, rename_map)
        df_final = self.clean_municipio(df_renamed, "municipio")

        df_final.to_csv(output_path, index=False, encoding="utf-8")
        
        print(f"Saved: {output_path} | Rows: {len(df_final)} | Columns: {list(df_final.columns)}")

    def run(self):
        """
        Executes the full IBGE data processing pipeline.
        """
        self.process_and_save(
            input_file="pib_municipios.csv",
            output_file="pib_clean.csv",
            rename_map=self.RENAME_MAP_PIB
        )

        self.process_and_save(
            input_file="populacao_municipios.csv",
            output_file="populacao_clean.csv",
            rename_map=self.RENAME_MAP_POPULATION
        )

if __name__ == "__main__":
    processor = IBGEProcessor()
    processor.run()