import streamlit as st 
import numpy as np 
import pandas as pd 
import time 
import plotly.express as px 


# csv repo de github
df = pd.read_csv("https://raw.githubusercontent.com/jpcorona/demoData/main/datos.csv")


st.set_page_config(
    page_title = 'Dashboard Tiempo Real',
    page_icon = '✅',
    layout = 'wide'
)

# titulo dashboard

st.title("Dashboard Tiempo Real")

# filtros

filtro_profesion = st.selectbox("Seleccione profesion", pd.unique(df['profesion']))


# creando un contenedor
placeholder = st.empty()

# filtro dataframe

df = df[df['profesion']==filtro_profesion]

# NRTP / simulacion feed rt 

for seconds in range(200):
#while True: 
    
    df['nueva_edad'] = df['edad'] * np.random.choice(range(1,5))
    df['nuevo_balance'] = df['balance'] * np.random.choice(range(1,5))

    # creando KPIs 
    avg_edad = np.mean(df['nueva_edad']) 

    contador_casados = int(df[(df["estado_civil"]=='casado')]['estado_civil'].count() + np.random.choice(range(1,30)))
    
    balance = np.mean(df['nuevo_balance'])

    with placeholder.container():
        # crear 3 columnas
        kpi1, kpi2, kpi3 = st.columns(3)

        # métricas o KPI
        kpi1.metric(label="KPI 1 ⏳", value=round(avg_edad), delta= round(avg_edad) - 10)
        kpi2.metric(label="KPI 2", value= int(contador_casados), delta= - 10 + contador_casados)
        kpi3.metric(label="KPI 3 ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/contador_casados) * 100)

        #columnas para los gráficos 

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### Gráfico 1")
            fig = px.density_heatmap(data_frame=df, y = 'nueva_edad', x = 'estado_civil')
            st.write(fig)
        with fig_col2:
            st.markdown("### Gráfico 2")
            fig2 = px.Histogram(data_frame = df, x = 'nueva_edad')
            st.write(fig2)
        st.markdown("### Vista detallada / data")
        st.dataframe(df)
        time.sleep(1)
    #placeholder.empty()
