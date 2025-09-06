import sidrapy
import pandas as pd
from pathlib import Path

def run():
    # Define a pasta de destino
    pasta = Path("data/raw/")
    pasta.mkdir(parents=True, exist_ok=True)

    # PIB dos Municípios (tabela 5938, variável 37 = PIB a preços correntes)
    df_pib = sidrapy.get_table(
        table_code="5938",
        territorial_level="6",        # municípios
        ibge_territorial_code="all",
        variable="37",                # PIB 
        period="last 1",              # último ano disponível
        header="n",
        format="pandas",
    )
    out_pib = pasta / "pib_municipios.csv"
    df_pib.to_csv(out_pib, index=False, encoding="utf-8")
    print(df_pib.shape, "- salvo em", out_pib.resolve())



    # População dos Municípios (tabela 6579)
    df_pop = sidrapy.get_table(
        table_code="6579",
        territorial_level="6",        # municípios
        ibge_territorial_code="all",
        period="last 1",
        header="n",
        format="pandas",
    )
    out_pop = pasta / "populacao_municipios.csv"
    df_pop.to_csv(out_pop, index=False, encoding="utf-8")
    print(df_pop.shape, "- salvo em", out_pop.resolve())

if __name__ == "__main__":
    run()


