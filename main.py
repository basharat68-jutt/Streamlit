import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your fav. ariety of chai")

chai = st.selectbox("Your fa chai: ",["Vital","K2","Lemon","Adrak Chai","Kesar Chai"])
st.write(f"Your choose{chai}. Excellent Choice!")

st.success("Your Chai has been brewed")


st.header("Select Your Fav Language")
language = st.selectbox("",["C++","Java","C#","Python"])
st.success(f"You Choose {language} Excellent Bro!")