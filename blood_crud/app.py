import streamlit as st
from blood_db import DonorCRUD
from datetime import date


tab1,tab2,tab3,tab4,tab5 = st.tabs(['ADD','READ','RETRIEVE','DELETE','UPDATE'])
d = DonorCRUD()

with tab1:
    st.title("Add a Donor")
    name = st.text_input("Name")
    blood_group = st.text_input("Blood Group")
    phone = st.number_input("Phone Number",min_value=0)
    city = st.text_input("City")
    last_donation = st.date_input("Last Donation Date")
    btn = st.button("ADD")

    if btn:
        d.post(name,blood_group,phone,city,last_donation)
        st.success("Record Added Successfully")

with tab2:
    st.title("View All Donors")
    records = d.get()
    print("hello")
    print(records)

    st.table(records)
#
with tab3:
    st.title("Retrieve Specific Donor")
    id = st.number_input("Donor ID", min_value=0)
    btn = st.button("Retrieve")

    if btn:
        record = d.retrieve(id)
        print(record)
        if record:
            st.write("Name:", record[1])
            st.write("Blood Group:", record[2])
            st.write("Phone:", record[3])
            st.write("City:", record[4])
            st.write("last Donation:", record[5])
        else:
            st.error("No Records Found")
#
with tab4:
    st.title("Delete Donor")
    id = st.number_input("Donor ID ", min_value=0)
    btn = st.button("DELETE")

    if btn:
        status = d.delete(id)
        if status:
            st.success("Record Deleted Successfully")
        else:
            st.error("No Records Found")

with tab5:
    st.title("Update Donor Details")
    id = st.number_input("Donor ID  ", min_value=0)
    name = st.text_input("Name ")
    blood_group = st.text_input("Blood Group ")
    phone = st.number_input("Phone Number ", min_value=0)
    city = st.text_input("City ")
    last_donation = st.date_input("Last Donation Date ")
    btn = st.button("UPDATE")

    if btn:
        status = d.put(name, blood_group, phone, city, last_donation,id)
        if status:
            st.success("Record Updated Successfully")
        else:
            st.error("No Records Found")