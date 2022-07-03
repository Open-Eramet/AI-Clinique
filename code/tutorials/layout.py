import streamlit as st
import numpy as np


with st.sidebar:
    st.header("Latéral/principal")
    state = st.checkbox("Checkbox")
    st.write(state)


st.header("Column")
col1, col2 = st.columns(2)

data = 10*np.cumsum(np.random.randn(10000))
with col1:
    st.line_chart(data)

hist, _ = np.histogram(data, bins=10)
col2.bar_chart(hist)

placeholder = st.empty()

st.header("Container")
with st.container():
    number = st.number_input("Saisir nombre")
    st.write(number)


st.header("Expander")
with st.expander("Details"):
    texte = st.text_input("Saisir texte")
    st.write(texte)
with placeholder:
    st.write("Placeholder !")




