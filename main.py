import sys
from pathlib import Path

# adiciona a raiz ao sys.path
sys.path.append(str(Path(__file__).parent))

from src.extract import ibge, sim

def main():
    print("[main] iniciando downloads…")
    ibge.run()   
    sim.run()  
    print("[main] concluído.")

if __name__ == "__main__":
    main()
