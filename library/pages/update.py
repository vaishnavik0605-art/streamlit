import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete


st.title("Update Book Record")
id = st.number_input("Book ID",min_value=0)
title = st.text_input("Title")
author = st.text_input("Author")
price = st.number_input("Price",min_value=0)
pages = st.number_input("Pages",min_value=0)
lang = st.text_input("Language")
btn = st.button("Update Book")

if btn:
    b = BookListCreateRetrieveUpdateDelete()
    status = b.update(id,title,author,price,pages,lang)
    if status:
        st.success("Record Updated Successfully")
    else:
        st.error("No Records Found")
