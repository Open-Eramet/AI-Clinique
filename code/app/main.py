import streamlit as st
from utils import *
from config import *

st.title("AI Clinique: Demo App")


with st.expander("01 - Charger le jeu de données"):
    pass
with st.sidebar:
    file = st.file_uploader("Upload")

if file:
    raw_dataset = pd.read_csv(file, sep=";")
    st.write(dataset)

st.header("02- Analyse exploratoire")
st.header("03- Pré-traitement & Nettoyage")
# st.info("Processing ...")
# dataset = preprocess(file)
# st.success("Fichier traité!")
st.header("04-Entrainement des modèles ML")

st.header("04-Evaluation")

    




