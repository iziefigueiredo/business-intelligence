# Project structure
```
business-intelligence/
├─ data/
│  ├─ raw/           # dados originais
│  ├─ interim/       # resultados intermediários
│  └─ processed/     # finais tratados para BI
│
├─ src/
│  ├─ __init__.py
│  ├─ utils.py       # funções de apoio
│
├─ extract/
│  ├─ __init__.py
│  ├─ ibge.py
│  ├─ sim.py
│
├─ transform/
│  ├─ __init__.py
│  ├─ process_*.py
│
├─ merge/
│  ├─ __init__.py
│  └─ cnes_sih.py
│
├─ tests/            # (opcional, pode ter __init__.py também)
│
├─ docs/             # relatórios e descrições do projeto
│
├─ main.py
├─ .gitignore
├─ README.md
└─ requirements.txt



```
