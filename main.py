import pandas as pd
import numpy as np
import streamlit as st
import plotly_express as px
from PIL import Image

header = st.container()
datasets = st.container()
interactive = st.container()

with header:
    st.title("Bienvenue sur le tableau de bord de l'etude WOCBP MRTC-Ouelessebougou")

st.write('''
# Visaulizer vos donnees sous forme de graph interactif 
''')

excel_file = 'C:/Users/lmiv/Documents/Kaggle/ECG.xlsx'
sheet_name = 'ecg'

df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols='B:H', header=0)

st.dataframe(df)
st.write('''#Diagramme de bar pour ECG Fait''')
ECG_Fait = pd.DataFrame(df['ECGYN'].value_counts())
st.bar_chart(ECG_Fait)

st.write('''Diagramme pour la normalite de ECG''')

ECG_Norm = pd.DataFrame(df['ECGORRES'].value_counts())
st.bar_chart(ECG_Norm)