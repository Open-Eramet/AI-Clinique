import pandas as pd
import datetime as dt
import streamlit as st
from config import *
from sklearn.model_selection import (
    TimeSeriesSplit,
    cross_validate,
)
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import ElasticNet, LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.dummy import DummyRegressor
from sklearn.tree import DecisionTreeRegressor
import numpy as np
import plotly.express as px
import os


def add_features(dataset, max_lag):

    features = dataset.copy()
    for lag in range(1, max_lag + 1):
        for feature in SELECTED_FEATURES + [TARGET]:
            features[f"{feature}_lag_{lag}"] = features[feature].shift(lag)
    n_new_features = max_lag * len(SELECTED_FEATURES)
    features = features.drop(SELECTED_FEATURES, axis=1).dropna().reset_index(drop=True)
    st.info(f"{n_new_features} nouvelles features crées")
    st.write(features.head())
    return features


def sidebar_elements():

    with st.sidebar:

        os.chdir(PROJECT_PATH)
        logo_path = os.path.join("docs", "logo.png")
        st.title(APP_NAME)
        st.image(logo_path, width=200)
        file = st.file_uploader("Charger les données")

        st.subheader("Afficher:")
        display_eda = st.checkbox("Analyse exploratoire (EDA)")
        display_feature_eng = st.checkbox("Feature Engineering")
        display_ml = st.checkbox("Expériences modèles ML")
        display_evaluation = st.checkbox("Evaluation")

    return file, display_eda, display_feature_eng, display_ml, display_evaluation


def display_timeseries(dataset):
    fig = px.line(dataset, x="date", y=dataset[SELECTED_FEATURES].columns)
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(xaxis_title="Date", yaxis_title="Prix ($)")
    st.plotly_chart(fig, use_container_width=True)


def add_date(row):
    """Add a date column"""
    month = row["Month"]
    year = int(row["Year"])
    date = dt.datetime.strptime(f"01 {month} {year}", "%d %b %Y")
    return date


@st.cache()
def preprocess(file_path):

    """
    TODO: Implement the followings steps:
    - Delete rows with Null month and year
    - Add date column (assume all dates are 1st day of month)
    - Sort by chronological order and index by date
    - Keep only inflation-corrected features
    - Fill NULL with foreward filling and drop any remaining NULLs
    """

    dataset = pd.read_csv(file_path, sep=";")
    dataset = dataset.dropna(subset=["Year", "Month"])
    dataset["date"] = dataset.apply(add_date, axis=1)
    dataset = (
        dataset.sort_values("date")
        .set_index("date")
        .loc[:, SELECTED_FEATURES + [TARGET]]
        .fillna(method="ffill")
        .dropna()
        .reset_index()
    )
    return dataset


def rmse(y_true, y_pred):

    return np.sqrt(mean_squared_error(y_true, y_pred))


def get_cv_score(dataset, pipeline, target):

    cv_score = cross_validate(
        estimator=pipeline,
        X=dataset.drop([target, "date"], axis=1).values,
        y=dataset[target].values,
        scoring=make_scorer(rmse, greater_is_better=False),
        cv=TimeSeriesSplit(n_splits=5),
        return_train_score=True,
    )

    train_score = -np.array(cv_score["train_score"])
    valid_score = -np.array(cv_score["test_score"])

    return train_score, valid_score


def get_predictions(dataset, pipeline, target):

    n = dataset.shape[0]
    train_size = int(n * 0.8)
    train = dataset.loc[: train_size - 1, :].drop("date", axis=1)
    valid = dataset.loc[train_size:, :].drop("date", axis=1)

    X_train, y_train = train.drop(target, axis=1).values, train[target].values
    X_valid, y_valid = valid.drop(target, axis=1).values, valid[target].values

    pipeline.fit(X_train, y_train)
    train_preds = pd.DataFrame({"y_pred": pipeline.predict(X_train), "y_true": y_train})
    valid_preds = pd.DataFrame({"y_pred": pipeline.predict(X_valid), "y_true": y_valid})
    predictions = pd.concat([train_preds, valid_preds], axis=0).reset_index(drop=True)
    predictions["date"] = dataset["date"].values
    return predictions


PIPELINES = {
    "linear_reg_std_scaling": Pipeline(
        [("scaler", StandardScaler()), ("regressor", LinearRegression())]
    ),
    "elastic_net_std_scaling": Pipeline(
        [("scaler", StandardScaler()), ("regressor", ElasticNet())]
    ),
    "decision_tree": Pipeline([("regressor", DecisionTreeRegressor())]),
    "random_forest": Pipeline([("regressor", RandomForestRegressor())]),
    "dummy-mean": Pipeline([("regressor", DummyRegressor(strategy="mean"))]),
    "dummy-median": Pipeline([("regressor", DummyRegressor(strategy="median"))]),
}


if __name__ == "__main__":

    dataset = preprocess(PROJECT_PATH / "data" / "input" / "dataset.csv")
    pipelines = PIPELINES
    for p in pipelines:
        pipeline = pipelines[p]
        train_score, valid_score = get_cv_score(
            dataset, pipeline=pipeline, target=TARGET
        )
        print(p, train_score, valid_score)
        predictions = get_predictions(dataset, pipeline=pipeline, target=TARGET)
