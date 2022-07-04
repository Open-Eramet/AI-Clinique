import pandas as pd
import datetime as dt
import streamlit as st
from config import *
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.dummy import DummyRegressor
import numpy as np


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
    - to make 1M ahead predictions, shift data 1M into the past
    - Fill NULL with foreward filling and drop any remaining NULLs
    """

    SELECTED_FEATURES = [
        "Price_alum_infl",
        "Price_gold_infl",
        "Price_nickel_infl",
        "Price_silver_infl",
        "Price_uran_infl",
    ]

    dataset = pd.read_csv(file_path, sep=";")
    dataset = dataset.dropna(subset=["Year", "Month"])
    dataset["date"] = dataset.apply(add_date, axis=1)
    dataset = (
        dataset.sort_values("date")
        .set_index("date")
        .loc[:, SELECTED_FEATURES]
        .shift(periods=1)
        .fillna(method="ffill")
        .dropna()
    )
    return dataset


def rmse(y_true, y_pred):

    return np.sqrt(mean_squared_error(y_true, y_pred))


def get_cv_score(dataset, pipeline, target):

    cv_score = cross_val_score(
        estimator=pipeline,
        X=dataset.drop(target, axis=1),
        y=dataset[target],
        scoring=make_scorer(rmse, greater_is_better=False),
        cv=TimeSeriesSplit(),
    )

    return -np.array(cv_score)


pipelines = {
    "linear_reg_std_scaling": Pipeline(
        [("scaler", StandardScaler()), ("regressor", LinearRegression())]
    ),
    "random_forest": Pipeline([("regressor", RandomForestRegressor())]),
    "dummy-mean": Pipeline([("regressor", DummyRegressor(strategy="mean"))]),
    "dummy-median": Pipeline([("regressor", DummyRegressor(strategy="median"))]),

}


if __name__ == "__main__":

    dataset = preprocess(PROJECT_PATH / "data" / "input" / "dataset.csv")
    for p in pipelines:
        pipeline = pipelines[p]
        cv_score = get_cv_score(dataset, pipeline=pipeline, target=TARGET)
        print(p, cv_score, cv_score.mean(), cv_score.std())