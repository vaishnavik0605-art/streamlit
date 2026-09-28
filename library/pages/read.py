import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Read All Book Record")

b = BookListCreateRetrieveUpdateDelete()
records = b.list()
print("hello")
print(records)

st.table(records)

