# Project structure
```
business-intelligence/
├─ data/
│  ├─ raw/         # dados originais
│  ├─ interim/     # resultados intermediários
│  └─ processed/     # finais tratados para BI
│
├─ src/
│  ├─ utils.py     # funções de apoio
│  └─ steps/       # cada etapa em um arquivo
│     ├─ 01_extract_*.py
│     ├─ 02_extract_*.py
│     ├─ 05_treat_*.py
│     ├─ 06_treat_*.py
│     └─ 09_merge_*.py
│
├─ tests/          # (opcional)
│
├─ docs/           # relatórios e descrições do projeto
│
├─ main.py         
├─ .gitignore
├─ README.md
└─ requirements.txt


```
