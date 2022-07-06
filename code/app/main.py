import streamlit as st
import plotly.express as px

from utils import *
from config import *

st.set_page_config(layout="wide", page_title=APP_NAME)


(
    file,
    display_eda,
    display_feature_eng,
    display_ml,
    display_evaluation,
) = sidebar_elements()

if not file:
    st.info("Charger les données sur le panneau latéral")
else:
    processed = preprocess(file)
    if display_eda:
        st.header("Analyse exploratoire (EDA)")
        display_timeseries(processed)
        col_1, col_2 = st.columns(2)
        col_1.subheader("Résumé")
        col_1.write(processed.describe())
        col_2.subheader("Matrice de corrélation")
        correlation = processed.drop("date", axis=1).corr().round(decimals=1)
        fig = px.imshow(correlation, text_auto=True)
        col_2.write(fig)

    if display_feature_eng:
        st.header("Feature Engineering")
        with st.sidebar:
            max_lag = int(st.slider("Historique", min_value=3, max_value=6))
        features = add_features(processed, max_lag)

    if display_ml:
        st.header("Expériences modèles ML")
        with st.sidebar:
            st.write("Sélectionner:")
            pipelines = st.multiselect(
                "Pipelines à tester", options=list(PIPELINES.keys())
            )
        if pipelines:
            results = []
            for pipeline in pipelines:
                train_score, valid_score = get_cv_score(
                    features, pipeline=PIPELINES[pipeline], target=TARGET
                )
                pipeline_results = pd.DataFrame(
                    {
                        "train score": train_score,
                        "valid score": valid_score,
                        "pipeline": pipeline,
                    }
                )
                results.append(pipeline_results)
            results = pd.concat(results, axis=0)
            train_fig = px.box(data_frame=results, x="pipeline", y="train score")
            valid_fig = px.box(data_frame=results, x="pipeline", y="valid score")
            train_col,valid_col = st.columns(2)
            train_col.plotly_chart(train_fig)
            valid_col.plotly_chart(valid_fig)

    if display_evaluation:

        st.header("Evaluation")
        if display_ml and len(pipelines) > 0:
            pipeline = results.groupby("pipeline")["valid score"].mean().idxmin()
            predictions = get_predictions(
                features, pipeline=PIPELINES[pipeline], target=TARGET
            )

            _, col_1, col_2, _ = st.columns(4)
            col_1.metric("Train: Moy. RMSE ($)", train_score.mean().round(1))
            col_2.metric("Valid: Moy. RMSE ($)", valid_score.mean().round(1))
            predictions_fig = px.line(data_frame=predictions, x="date", y=["y_pred", "y_true"])
            st.plotly_chart(predictions_fig, use_container_width=True)
