import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

tab1,tab2,tab3,tab4,tab5 = st.tabs(['ADD','READ','RETRIEVE','DELETE','UPDATE'])
b = BookListCreateRetrieveUpdateDelete()

with tab1:
    st.title("ADD")
    title = st.text_input("Title")
    author = st.text_input("Author")
    price = st.number_input("Price", min_value=0)
    pages = st.number_input("Pages", min_value=0)
    lang = st.text_input("Language")
    btn = st.button("Add Book")

    if btn:
        # b = BookListCreateRetrieveUpdateDelete()
        b.create(title, author, price, pages, lang)
        st.success("Record Created Successfully")

with tab2:
    st.title("READ")
    # b = BookListCreateRetrieveUpdateDelete()
    records = b.list()
    print("hello")
    print(records)

    st.table(records)

with tab3:
    st.title("RETRIEVE")
    id = st.number_input("Book ID", min_value=0)
    btn = st.button("Retrieve")

    if btn:
        # b = BookListCreateRetrieveUpdateDelete()
        record = b.retrieve(id)
        print(record)
        if record:
            st.write("Title:", record[1])
            st.write("Author:", record[2])
            st.write("Price:", record[3])
            st.write("Pages:", record[4])
            st.write("Languages:", record[5])
        else:
            st.error("No Records Found")

with tab4:
    st.title("DELETE")
    id = st.number_input("Book ID", min_value=0)
    btn = st.button("Delete Book")

    if btn:
        # b = BookListCreateRetrieveUpdateDelete()
        status = b.delete(id)
        if status:
            st.success("Record Deleted Successfully")
        else:
            st.error("No Records Found")

with tab5:
    st.title("UPDATE")
    id = st.number_input("Book ID", min_value=0)
    title = st.text_input("Title")
    author = st.text_input("Author")
    price = st.number_input("Price", min_value=0)
    pages = st.number_input("Pages", min_value=0)
    lang = st.text_input("Language")
    btn = st.button("Update Book")

    if btn:
        # b = BookListCreateRetrieveUpdateDelete()
        status = b.update(id, title, author, price, pages, lang)
        if status:
            st.success("Record Updated Successfully")
        else:
            st.error("No Records Found")