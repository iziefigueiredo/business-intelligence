# main.py
import sys
from pathlib import Path

# Adiciona a raiz do projeto ao sys.path para que as importações funcionem
# Isso garante que você pode importar 'src.pipeline_sim' de qualquer lugar
project_root = str(Path(__file__).parent)
if project_root not in sys.path:
    sys.path.append(project_root)

# Importa as funções de cada pipeline
from src.pipeline_sim import run_pipeline_sim
# from src.pipeline_ibge import run_pipeline_ibge # Adicione essa linha quando criar o arquivo

def menu():
    """
    Exibe um menu para executar os pipelines.
    """
    while True:
        print("\n=== MENU BI - ORQUESTRADOR ===")
        print("[1] Executar Pipeline do SIM")
        print("[2] Executar Pipeline do IBGE")
        print("[0] Sair")
        print("=" * 30)

        escolha = input("Escolha a etapa que deseja executar: ").strip()

        try:
            if escolha == "1":
                run_pipeline_sim()
            elif escolha == "2":
                print("Pipeline do IBGE ainda não implementado. Por favor, escolha a opção 1.")
                # run_pipeline_ibge() # Descomente essa linha quando o arquivo for criado
            elif escolha == "0":
                print("Encerrando o orquestrador.")
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("\n" + "=" * 30)
            print(f"ERRO NA EXECUÇÃO: {e}")
            print("=" * 30)


if __name__ == "__main__":
    menu()