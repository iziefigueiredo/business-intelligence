# main.py — menu simples: [1] Extrair dados | [2] Tratar dados (comentado)
import sys
from pathlib import Path
from importlib import import_module

# garante que a raiz do projeto está no sys.path
sys.path.insert(0, str(Path(__file__).parent.resolve()))

def run_callable(spec: str):
    """
    spec no formato 'pacote.modulo:funcao'
    ex.: 'src.extract.ibge:run'
    """
    mod_name, func_name = spec.split(":")
    mod = import_module(mod_name)
    fn = getattr(mod, func_name)
    fn()

# ==== pipelines =====
EXTRACT_STEPS = [
    "src.extract.ibge:run",
    "src.extract.sim:run",
]

# TRANSFORM_STEPS = [
#     "src.transform.processing_sim:run",
#     "src.transform.processing_sim:run",
#     
# ]

def menu():
    while True:
        print("\n=== MENU BI ===")
        print("[1] Extrair dados (IBGE + SIM)")
        print("[2] Tratar dados ")
        print("[0] Sair")
        op = input("Escolha: ").strip()

        if op == "0":
            break
        elif op == "1":
            for spec in EXTRACT_STEPS:
                run_callable(spec)
        elif op == "2":
            print("Opção de tratamento ainda desabilitada.")
            # for spec in TRANSFORM_STEPS:
            #     run_callable(spec)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
