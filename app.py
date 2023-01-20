import streamlit as st 
import numpy as np 
import pandas as pd 
import time 
import plotly.express as px 


# csv repo de github
df = pd.read_csv("https://raw.githubusercontent.com/jpcorona/demoAgrosuper/main/datos.csv")


st.set_page_config(
    page_title = 'Dashboard Tiempo Real',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Dashboard Tiempo Real")

# top-level filters 

job_filter = st.selectbox("Seleccione profesion", pd.unique(df['job']))


# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

df = df[df['profesion']==job_filter]

# near real-time / live feed simulation 

for seconds in range(200):
#while True: 
    
    df['age_new'] = df['edad'] * np.random.choice(range(1,5))
    df['balance_new'] = df['balance'] * np.random.choice(range(1,5))

    # creating KPIs 
    avg_age = np.mean(df['age_new']) 

    count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))
    
    balance = np.mean(df['balance_new'])

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs 
        kpi1.metric(label="KPI 1 ⏳", value=round(avg_age), delta= round(avg_age) - 10)
        kpi2.metric(label="KPI 2", value= int(count_married), delta= - 10 + count_married)
        kpi3.metric(label="KPI 3 ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_married) * 100)

        # create two columns for charts 

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### Gráfico 1")
            fig = px.density_heatmap(data_frame=df, y = 'age_new', x = 'marital')
            st.write(fig)
        with fig_col2:
            st.markdown("### Gráfico 2")
            fig2 = px.histogram(data_frame = df, x = 'age_new')
            st.write(fig2)
        st.markdown("### Vista detallada / data")
        st.dataframe(df)
        time.sleep(1)
    #placeholder.empty()
