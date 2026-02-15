import streamlit as st
import pandas as pd

st.title("Care Transition Efficiency Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Convert numeric columns to numbers
    cols = ["Children transferred out of CBP custody","Children in CBP custody","Children discharged from HHS Care","Children in HHS Care"]

    for col in cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Create efficiency metrics
    df["Transfer_Efficiency"] = (df["Children transferred out of CBP custody"] /df["Children in CBP custody"])

    df["Discharge_Efficiency"] = (df["Children discharged from HHS Care"] /df["Children in HHS Care"])

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Key Performance Indicators")

    col1, col2 = st.columns(2)

    col1.metric("Avg Transfer Efficiency",round(df["Transfer_Efficiency"].mean(), 2))

    col2.metric("Avg Discharge Efficiency",round(df["Discharge_Efficiency"].mean(), 2))

    st.subheader("Efficiency Trends")

    st.line_chart(df.set_index("Date")[["Transfer_Efficiency","Discharge_Efficiency"]])