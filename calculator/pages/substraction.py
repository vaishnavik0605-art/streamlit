import streamlit as st

st.title("Substraction")
num1 = st.number_input("Enter first number",min_value=0)
print(num1)
num2 = st.number_input("Enter second number",min_value=0)
print(num2)
btn = st.button("Substract")
if btn:
    result = num1 - num2
    print(result)
    st.write("Difference is",result)