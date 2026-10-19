import streamlit as st
import requests

st.title("Live Currency Converter")
amount = st.number_input("Enter the Amount in PKR",min_value=1)
target_currency = st.selectbox("Convert To",['INR','USD','EUR',"GBP",'JPY'])

if st.button("Convert"):
     url = "https://api.exchangerate-api.com/v4/latest/INR"
     response = requests.get(url)

     if response.status_code == 200:
        data = response.json()
        rate = data['rates'][target_currency]
        converted = rate * amount
        st.success(f"{amount} INR = {converted:.2f}")
     else:
          st.error("Failed To Fetch Conversion Rate")
     
