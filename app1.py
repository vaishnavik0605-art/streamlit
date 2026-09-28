import streamlit

streamlit.title("My First App")
name = streamlit.text_input("Enter name")
streamlit.write(name)
place = streamlit.radio("Select location",['ekm','tvm','mlp'])
streamlit.write(place)