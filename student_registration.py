import streamlit as st
from datetime import date

st.title("Student Registration Form")
name = st.text_input("Name")
age = st.number_input("Age",min_value=0)
dob = st.date_input("DOB",min_value=date(1970,1,1),max_value=date.today(),value=date(2000,1,1))
email = st.text_input("Email")
gender = st.radio("Select Gender",['Male','Female'])
courses = st.selectbox("Select Course",['python','java','dotnet','testing'])
btn = st.button("Register")
if btn:
    st.subheader("Student Details")
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("DOB:",dob)
    st.write("Email:",email)
    st.write("Gender:",gender)
    st.write("Course:",courses)