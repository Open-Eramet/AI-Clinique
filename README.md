# ERAMET AI Clinique

### Commt prototyper et déployer des web applications Data/ML avec Steamlit ?

--------

### 💻 Setup

0 - S'assurer d'avoir Python et Conda comme gestionnaire d'environnements:
Si ce n'est pas le cas, installer Python via Miniconda en suivant ces instructions: https://docs.conda.io/en/latest/miniconda.html en suivant les instructions selon votre OS.

1 - Lancer un terminal miniconda et exécuter les commandes suivantes

a - Cloner ce dépôt Git

```bash
git clone https://github.com/Open-Eramet/AI-Clinique.git
cd AI-Clinique
```

b- Créer un environnement virtuel selon requirements.txt. Pour ce faire, 

```bash
conda create -n ai-clinique python==3.8.13
conda activate ai-clinique
pip install -r requirements.txt
```

(Optionel)
- Pour le déploiment en Applications Streamlit en Standalone, il faut installer:
    - NSIS
    - le package Python pynist en suivant les instructions dans ce Readme https://github.com/takluyver/pynsist

### 📉 Data
Le jeu de donnée utilisé représente l'historique de cours de quelques métaux tels que l'Or, Aluminium, Argent, Nickel et Uranium. Ces données sont publiées sur Kaggle [Ici](https://www.kaggle.com/datasets/timmofeyy/-metals-price-changes-within-last-30-years) en Open Data.

Nous avons choisi ce jeu de données en relation avec l'Activité d'Eramet comme un principal producteur  de Nickel dans le monde. Pour plus de détails/contexte voir [Lien](https://www.eramet.com/fr/activites/produits/nickel)


### Data description

- __Year__: annee
- __Month__: mois
- __Price_alum__: Prix Aluminium ($/Tonne)
- __Price_gold__: Prix Or ($/Once Troy)
- __Price_nickel__: Prix Nickel ($/Tonne)
- __Price_silver__: Prix Argent ($/Once Troy)
- __Price_uran__: Prix Uranium ($/livre)
- __Inflation_rate__: Taux d'inflation pour correction de prix (%)
- __Price_alum_infl__: Prix Aluminium réajusté ($/Tonne)
- __Price_gold_infl__: Prix Or réajusté ($/Once Troy)
- __Price_nickel_infl__: Prix Nickel  réajusté ($/Tonne)
- __Price_silver_infl__: Prix Argent réajusté ($/Once Troy)
- __Price_uran_infl__: Prix Uranium réajusté ($/livre)

## 📁 Organisation:
```
│   .gitignore
│   README.md
├───code
│   ├───app
│   │
│   └───tutorials
│           display.py
│           layouts.py
│           widgets.py
│
└───data
    ├───input
    │       dataset.csv
    └───output
```
