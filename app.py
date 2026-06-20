import streamlit as st
import pandas as pd
import os

st.title("AI Food Donation Assistant")

food_name = st.text_input("Food Name")
quantity = st.number_input("Quantity", min_value=1)
food_type = st.selectbox("Food Type", ["Veg", "Non-Veg"])
location = st.text_input("Location")

if st.button("Donate Food"):
    data = {
        "Food Name": [food_name],
        "Quantity": [quantity],
        "Food Type": [food_type],
        "Location": [location]
    }

    df = pd.DataFrame(data)

    if os.path.exists("donations.csv"):
        df.to_csv("donations.csv", mode="a", header=False, index=False)
    else:
        df.to_csv("donations.csv", index=False)

    st.success("Food Donation Added Successfully!")

if os.path.exists("donations.csv"):
    df = pd.read_csv("donations.csv")

    st.subheader("All Donations")

    filter_type = st.selectbox(
        "Filter Donations",
        ["All", "Veg", "Non-Veg"]
    )

    if filter_type != "All":
        df = df[df["Food Type"] == filter_type]

    st.dataframe(df)

    st.metric("Total Donations", len(df))