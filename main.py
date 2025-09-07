# main.py — menu de etapas do pipeline
import sys
from pathlib import Path

# --- Importações diretas dos módulos de todo o pipeline ---
# Garante que as importações funcionem a partir da raiz do projeto
from src.extract import ibge, sim
from src.transform import processing_ibge, processing_sim
#from src.merge import unify

def menu():
    while True:
        print("\n=== MENU BI ===")
        print("[1] Extrair dados (IBGE e SIM)")
        print("[2] Tratar dados ")
        print("[0] Sair")
        op = input("Escolha: ").strip()

        if op == "0":
            break
        elif op == "1":
            print("=== Extrair dados ===")
            ibge.run()
            sim.run()
        elif op == "2":
            print("=== Tratar dados ===")
            # === Chamada direta das funções de tratamento ===
            processing_ibge.processar_salvar(
                arquivo_entrada="pib_municipios.csv",
                arquivo_saida="pib_limpo.csv",
                renome_map={
                    "V": "pib",
                    "D1N": "municipio",
                    "D1C": "cod_mun",
                    "D2C": "ano",
                }
            )
            processing_ibge.processar_salvar(
                arquivo_entrada="populacao_municipios.csv",
                arquivo_saida="populacao_limpo.csv",
                renome_map={
                    "V": "populacao",
                    "D1N": "municipio",
                    "D1C": "cod_mun",
                    "D2C": "ano",
                }
            )
            processing_sim.processar_sim()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()