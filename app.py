import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Interact with Gapminder")

df = pd.read_csv('gapminder_tidy.csv')

continent_list = list(df['continent'].unique())
metric_list = list(df['metric'].unique())

with st.sidebar:
    st.subheader("Configure the plot")
    continent = st.selectbox(label='Choose a continent', options=continent_list)
    metric = st.selectbox(label='Choose a metric', options=metric_list)

query = f"continent=='{continent}' & metric=='{metric}'"

df_gdp = df.query(query)

metric_labels = {'gdpPercap' : 'GDP Per Capita', 'lifeExp' : 'Average Life Expectancy', 'pop' : 'Population'}

title = f"{metric_labels[metric]} for countries in {continent}"
fig = px.line(df_gdp, x='year', y='value', color='country', title=title)

st.plotly_chart(fig, use_container_width=True)
