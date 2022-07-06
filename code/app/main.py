from matplotlib.pyplot import figimage
import streamlit as st
from utils import *
import plotly.express as px
from config import *

st.set_page_config(layout="wide", page_title="AI-Clinique-Demo-App")

with st.sidebar:
    st.title("AI Clinique: Demo App")
    file = st.file_uploader("Charger les données")
if file:
    st.header("Analyse exploratoire")
    processed = preprocess(file)
    display_chart = st.checkbox("Graphe")
    display_summary = st.checkbox("Résumé")
    display_correlation = st.checkbox("Corrélation")

    if display_chart:
        display_timeseries(processed)
    col_1, col_2 = st.columns(2)
    if display_summary:
        col_1.subheader("Résumé")
        col_1.write(processed.describe())
    if display_correlation:
        col_2.subheader("Matrice de corrélation")
        correlation = processed.drop("date", axis=1).corr().round(decimals=1)
        fig = px.imshow(correlation, text_auto=True)
        col_2.write(fig)

    st.header("Feature Engineering")

    with st.sidebar:
        max_lag = int(st.number_input("Historique", min_value=1, max_value=6))
        features = processed.copy()
        for lag in range(1, max_lag + 1):
            for feature in SELECTED_FEATURES + [TARGET]:
                features[f"{feature}_lag_{lag}"] = features[feature].shift(lag)
        n_new_features = max_lag * len(SELECTED_FEATURES)
        features = features.drop(SELECTED_FEATURES, axis=1).dropna()
        st.info(f"{n_new_features} nouvelles features crées")
    st.write(features.head())

    # st.info("Processing ...")
    # dataset = preprocess(file)
    # st.success("Fichier traité!")
    st.header("Entrainement des modèles ML")
    with st.sidebar:
        model = st.selectbox("Selectionner modèle", options = list(pipelines.keys()) )
    cv_score = get_cv_score(features, pipeline=pipelines[model], target=TARGET)
    st.header("Evaluation")
    _, col_1, col_2, _ = st.columns(4)
    col_1.metric("Moy. RMSE ($)", cv_score.mean().round(1))
    col_2.metric("Ecart type. RMSE ($)", cv_score.std().round(1))    
else:
    st.info("Charger les données sur le panneau latéral")
