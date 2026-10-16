import streamlit as st

st.title("Chai maker app")

if st.button("Make Chai"):
    st.success("Your Chaii Is being brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala Added")


tea_type = st.radio("Pick your chai base: ",['Milk','Water','Honey'])
st.write(f"Selected Item si {tea_type}")

sugar = st.slider("Sugar Level",0,5,2)

cups = st.number_input("How many cups",min_value=1,max_value=10,step=1)



from datetime import date
today = date.today()
dob = st.date_input("Enter Your Date",value=date(2000,1,1),min_value=date(1900,1,1),max_value=date.today())
st.write(f"Selected DOB is {dob}")

age = today.year - dob.year

st.write(f"You Are Age Of {age} Years")