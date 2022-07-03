import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


# Display funcs
## Text
st.text("Hello World !")
st.write("Bienvenue sur mon App !")

st.title("Concepts de bases")
st.header("Fonctions d'affichages")
st.subheader("Texte")
## Markdown
st.markdown("**Ce texte est en gras**")
st.markdown("*Celui-ci est en italique*")
st.markdown("## Titre 2")
st.markdown("### Titre 2.1")
st.markdown("#### Titre 2.1.1")


## Generic objects
st.markdown("------")
st.subheader("Objets de base")
st.write("List")
elements = ["a", "b", "c"]
st.write(elements)
st.write("Dict")
dico = {"a": 1, "b": 2, "c": 3}
st.write(elements)

st.text("Utiliser Magic !")
dico


## Logs
st.markdown("------")
st.subheader("Logs")
st.info("Ceci est un log type info")
st.warning("Ceci est un log type warning")
st.error("Ceci est un log type error")
st.success("SUCCESS !")


st.subheader("DataFrames")
URL = "https://raw.githubusercontent.com/Open-Eramet/AI-Clinique/master/data/input/dataset.csv"
dataset = pd.read_csv(URL, sep=";")
sample = dataset.head(5)
st.dataframe(sample)
st.info("st.dataframe affiche un contenu dynamique")
st.markdown("------")

st.table(sample)
st.info("st.table affiche une table statique")

st.markdown("------")
st.subheader("Graphes 📉")
serie = dataset["Price_alum"]
st.write("### Matplotlib")
fig, ax = plt.subplots()
ax.hist(serie)
st.pyplot(fig)

st.write("### VegaLite")
st.line_chart(serie)

st.write("### Plotly")
fig = px.line(serie)
fig
st.write("### Cartes 🗼")

map_data = pd.DataFrame(
    0.1 * np.random.randn(100, 2) + [48.856614, 2.3522219], columns=["lat", "lon"]
)

st.markdown("------")
st.subheader("Images/vidéos/etc ...")

st.image("https://static.streamlit.io/examples/cat.jpg")

st.map(map_data)
