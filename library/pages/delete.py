import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.title("Delete Book Record")

id = st.number_input("Book ID",min_value=0)
btn = st.button("Delete Book")

if btn:
    b = BookListCreateRetrieveUpdateDelete()
    status = b.delete(id)
    if status:
        st.success("Record Deleted Successfully")
    else:
        st.error("No Records Found")
