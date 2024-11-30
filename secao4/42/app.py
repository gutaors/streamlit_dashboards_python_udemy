import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import grafico_map_estado

st.set_page_config(layout='wide')
st.title("Dashboard de Vendas :shopping_trolley:")

aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
with aba1:
    st.dataframe(df)
