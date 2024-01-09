# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Leitura do arquivo CSV
car_data = pd.read_csv('vehicles.csv')

# Cabeçalho do aplicativo
st.header('Aplicativo de Análise de Vendas de Carros')

# Botão para criar um histograma
hist_button = st.button('Criar Histograma')

# Botão para criar um gráfico de dispersão
scatter_button = st.button('Criar Gráfico de Dispersão')

# Verifica se o botão de histograma foi clicado
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # Criar um histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

# Verifica se o botão de gráfico de dispersão foi clicado
if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # Criar um gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)

