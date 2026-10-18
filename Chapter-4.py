import streamlit as st
import pandas as pd


st.title("Chai Sales Dashboard")
file = st.file_uploader("Upload Your CSV File",type=['csv'])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preiew")
    st.dataframe(df)

if file:
    st.subheader("Summry States")
    st.write(df.describe())

if file:
    cities = df["City"].unique()
    selected_cities = st.selectbox("Filter by cities ",cities)
    filter_data = df[df['City'] == selected_cities]
    st.dataframe(filter_data)


