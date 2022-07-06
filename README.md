# ERAMET AI Clinique

### Comment prototyper et déployer des web app Data/ML avec Streamlit ?

--------
### ⭐ Contexte

La DataFoundry, unité Data Science au sein de la Direction de la [Transformation Numérique](https://www.eramet.com/fr/groupe/transformation-numerique) d'[Eramet](https://www.eramet.com/fr), propose un atelier pratique d'initiation à l'utilisation de [Streamlit](https://streamlit.io/)

Le but est de s'initier au prototypage de web app au travers de cas pratiques simples et de créer un moment d'échange au sein de la communauté Data.


### 💻 Setup

0 - S'assurer d'avoir installé Python et Conda (gestionnaire d'environnements virtuels).
Si ce n'est pas le cas, installer Python via Miniconda en suivant ces instructions selon votre OS: https://docs.conda.io/en/latest/miniconda.html.

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
Le jeu de données utilisé représente l'historique des cours de marché de quelques métaux tels que l'or, l'aluminium, l'argent, le nickel et l'uranium. Ces données sont librement accessibles et publiées sur Kaggle [ici](https://www.kaggle.com/datasets/timmofeyy/-metals-price-changes-within-last-30-years) en Open Data.

Nous avons choisi ce jeu de données en relation avec les activités minières d'Eramet, un des principaux producteurs de nickel dans le monde. Pour plus de détails voir [Activité nickel](https://www.eramet.com/fr/activites/produits/nickel)


### Data description

- __Year__: année
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
│   requirements.txt
│
├───code
│   ├───app
│   │   │   config.py               # Demo app à  développer ensemble
│   │   │   main.py
│   │   │   utils.py
│   └───tutorials                    # Tutoriels à faire ensemble
│           display.py
│           layout.py
│           widgets.py
│
├───data
│   ├───input
│   │       dataset.csv
│   │
│   └───output
└───docs
        logo.png
        presentation.py
        step_1.JPG                  # Exercices d'accompagnement Demo App
        step_2.JPG
        step_3.JPG
        step_4.JPG
        step_5.JPG
        Streamlit.png
```
