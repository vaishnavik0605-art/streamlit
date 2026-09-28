import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("Read a Specific Book Record")

id = st.number_input("Book ID",min_value=0)
btn = st.button("Retrieve")

if btn:
    b = BookListCreateRetrieveUpdateDelete()
    record = b.retrieve(id)
    print(record)
    if record:
        st.write("Title:",record[1])
        st.write("Author:",record[2])
        st.write("Price:",record[3])
        st.write("Pages:",record[4])
        st.write("Languages:",record[5])
    else:
        st.error("No Records Found")


