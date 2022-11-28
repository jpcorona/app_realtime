import streamlit as st 
import numpy as np 
import pandas as pd 
import time 
import plotly.express as px 


# csv repo de github
df = pd.read_csv("https://raw.githubusercontent.com/jpcorona/demoAgrosuper/main/datos.csv")


st.set_page_config(
    page_title = 'Panel en tiempo real modelo data science',
    page_icon = '✅',
    layout = 'wide'
)

# titulo panel

st.title("Panel en tiempo real - Modelo Data Science")

# filtros

area_filter = st.selectbox("Seleccione una area", pd.unique(df['area']))


# crear un contenedor

placeholder = st.empty()

# filtro del dataframe

df = df[df['area']==area_filter]

# NRTP / simulación de muestras en tiempo real

for seconds in range(200):
#while True: 
    
    df['rutas_atrasadas'] = df['ruta'] * np.random.choice(range(1,12)) 
    df['nuevo_balance'] = df['balance'] * np.random.choice(range(1,5)) 

    # creando el KPI

    avg_rutas= np.mean(df['rutas_atrasadas'])  #sacamos la media

    contador_casados = int(df[(df["estado_maquina"]=='buena')]['estado_maquina'].count() + np.random.choice(range(1,30)))
    
    balance = np.mean(df['nuevo_balance']) #sacamos la media

    with placeholder.container():
        # crear 3 columnas para los kpi
        kpi1, kpi2, kpi3 = st.columns(3)

        # complete esas tres columnas con las respectivas métricas o KPI 
        kpi1.metric(label="KPI 1 🐖", value=round(avg_rutas), delta= round(avg_rutas) - 10)
        kpi2.metric(label="KPI 2 🐔", value= int(contador_casados), delta= - 10 + contador_casados)
        kpi3.metric(label="KPI 3 🦃", value= f"$ {round(balance,2)} ", delta= - round(balance/contador_casados) * 100)

        # crear 2 columnas para graficos

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### Gráfico 1")
            fig = px.density_heatmap(data_frame=df, y = 'rutas_atrasadas', x = 'estado_maquina')
            st.write(fig)
        with fig_col2:
            st.markdown("### Gráfico 2")
            fig2 = px.histogram(data_frame = df, x = 'rutas_atrasadas')
            st.write(fig2)
        st.markdown("### Vista detallada de los datos")
        st.dataframe(df)
        time.sleep(1)
    #placeholder.empty()

