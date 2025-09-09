
# Business Intelligence Pipeline: Public Management Analysis
This project provides a robust data pipeline for a Business Intelligence solution focused on public management and territorial planning. The goal is to transform raw data from official sources like the Brazilian Institute of Geography and Statistics (IBGE) and DATASUS into actionable insights for public managers.

The pipeline is designed to be modular and scalable, following best practices for data engineering and software development.

Features
- Data Extraction: Automated scripts to download raw data from official APIs.

- Data Transformation: Scripts to clean, standardize, and enrich data for analysis.

- Data Unification: Modules to merge disparate datasets into a single, cohesive source.

- Exploratory Data Analysis (EDA): Scripts to generate data profiles and quality reports.

- Orchestration: A central main.py script to run the entire pipeline with a simple menu interface.

---
## Getting Started  

### Clone this repository
```
   git clone https://github.com/your-username/business-intelligence.git
```
```
   cd business-intelligence
```

### Create and activate a virtual environment  

```
python -m venv .venv

```

```
source .venv/bin/activate   # Linux/Mac

```

```
.venv\Scripts\activate      # Windows

```
### Install dependencies

```
pip install -r requirements.txt

```

### Run the pipeline  
```
python main.py
```

## Project structure
```
business-intelligence/
├─ data/
│  ├─ raw/           
│  ├─ interim/       
│  └─ processed/     
│
├─ src/
│  ├─ __init__.py
│  ├─ pipeline_sim.py       
│  ├─ pipeline_ibge.py
│
├─ extract/
│  ├─ __init__.py
│  ├─ ibge.py
│  ├─ sim.py
│
├─ transform/
│  ├─ __init__.py
│  ├─ processing_sim.py
│  ├─ processing_ibge.py
│
├─ merge/
│  ├─ __init__.py
│  ├─ unify_ibge.py
│  └─ unify_sim.py
│
├─ eda/
│  ├─ __init__.py
│  ├─ profile_sim.py
│  ├─ profile_ibge.py
│
├─ tests/            # (opcional, pode ter __init__.py também)
│
├─ docs/             # relatórios e descrições do projeto
│
├─ __init__.py
├─ main.py
├─ .gitignore
├─ README.md
└─ requirements.txt



```
