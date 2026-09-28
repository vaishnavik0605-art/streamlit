import streamlit as st

name = st.text_input("Name")
age = st.number_input("Age",min_value=0)
place = st.text_input("Place")
gender = st.radio("Select Gender",['Male','Female'])
qualifications = st.selectbox("Select Qualification",['bca','bba','btech'])
btn = st.button("Submit")

if btn:
    st.title("User Info")
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("Place:",place)
    st.write("Gender:",gender)
    st.write("Qualification:",qualifications)


