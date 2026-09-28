import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Add New Book Record")
title = st.text_input("Title")
author = st.text_input("Author")
price = st.number_input("Price",min_value=0)
pages = st.number_input("Pages",min_value=0)
lang = st.text_input("Language")
btn = st.button("Add Book")

if btn:
    b = BookListCreateRetrieveUpdateDelete()
    b.create(title,author,price,pages,lang)
    st.success("Record Created Successfully")