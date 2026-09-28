import streamlit as st

st.title("Multiplication")
num1 = st.number_input("Enter first number",min_value=0)
print(num1)
num2 = st.number_input("Enter second number",min_value=0)
print(num2)
btn = st.button("Multiply")
if btn:
    result = num1 * num2
    print(result)
    st.write("Product is",result)