import streamlit as st

st.title("BMI Calculator")
wt = st.number_input("Weight in kg",min_value=0)
print(wt)
ht = st.number_input("Height in cm",min_value=0)
print(ht)
btn = st.button("BMI")
if btn:
    result = wt / ((ht/100)**2)
    if result < 18.5:
        st.info("Underweight")
    elif result < 25 and result >= 18.5:
        st.success("Normal")
    elif result < 30 and result >= 25:
        st.warning("Overweight")
    elif result > 30:
        st.error("Obesity")