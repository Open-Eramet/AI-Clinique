import streamlit as st
import datetime as dt
import pandas as pd

st.header("User widgets")


st.subheader("Checkbox")
okay = st.checkbox("Check Option ?")
if okay:
    st.write("👍")
st.subheader("Radio")
option = st.radio("Options", options=list(range(3)))
st.write(f"Vous avez choisi l'option {option}")
st.subheader("SelectBox")
option = st.selectbox("Options", options=list(range(3)))
st.write(f"Vous avez choisi l'option {option}")
st.subheader("Multi-Select")
options = st.multiselect("Options", options=list(range(5)))
st.write(f"Vous avez choisi les options {options}")

st.subheader("Slider")
number = st.slider("Hyperparamètre", 0, 100)
st.write(f"Hyperparamètre = {number}")

st.subheader("Number input")
number = st.number_input("Nombre", min_value=0, max_value=10)
st.write(f"{number}")


st.subheader("Text input")
text = st.text_input("Entrer un texte")
st.write(f"Vous avez saisi: __{text}__")


st.subheader("Date input")
date = st.date_input("Entrer une Date", value=dt.date.today())
st.write(f"Vous avez saisi: __{date}__")

st.subheader("File uploader")
file = st.file_uploader("Charger un fichier")
if file:
    dataset = pd.read_csv(file, sep=";")
    st.write(dataset.head())

st.subheader("File Downloader")
if file:
    st.download_button(
        "Télécharger un fichier", data=file, file_name="exemple.csv", mime="text/csv"
    )
