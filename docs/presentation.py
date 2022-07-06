import streamlit as st

st.set_page_config(layout="wide", page_title="Presentation")

with st.expander("Programme"):

    message = """
    ### Introduction/contexte
    - Introduction: Eramet, contexte, Modop TN [10min] -> 10h10
    - Démos de quelques applis: Qu'est ce qui possible de faire avec Streamlit ? [10min] ->10h20
        - CMM Lining Fours
        - Applications de la communauté [https://streamlit.io/gallery](https://streamlit.io/gallery)
            - Exemple: [Streamlit Prophet](https://share.streamlit.io/maximelutel/streamlit_prophet/main/streamlit_prophet/app/dashboard.py)

    - Motivations: Pourquoi déployer/partager mes analyses data science/modèles [5min] -> 10h25
    ### Partie Hands-On
    - Présentation Des principaux concepts de Streamlit [15min] -> 10h40
    - Check technique (installation, problème wifi, libs)
    - Tour d’horizon des fonctionnalités [10min] -> 10h50
    
    - Pause: [15min]  11h05
    - Tour d’horizon des fonctionnalités (suite) [10min] -> 11h15
    - Mise en place d'une app ML end to end (exercices)  [30min]   
    - Options de déploiement [20min] -> 12:05
        - Streamlit Share
        - Heroku App
        - Création d’installeur Desktop (CMM)
    """

    st.markdown(message)

with st.expander("Introduction & Contexte Eramet"):

    st.image("docs/modop.png")

with st.expander("Demo App/Motivations"):

    st.markdown("""
    - [Gallerie de projets](https://streamlit.io/gallery)
    - __Suivi Lining Fours CMM__
    - __Streamlit Prophet__  [Site](https://share.streamlit.io/maximelutel/streamlit_prophet/main/streamlit_prophet/app/dashboard.py)
    
    """)

with st.expander("Présentation Streamlit"):

    st.image("docs/Streamlit.png")


