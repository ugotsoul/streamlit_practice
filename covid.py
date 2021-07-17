import streamlit as st
import pandas as pd
import altair as alt

st.title("COVID data by country")
st.text("Plots covid incidence rates by country")

url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"
df = pd.read_csv(url, index_col=0, parse_dates=True)

countries = df["Country"].unique()
country_choice = st.selectbox("", countries)

case_types = ["Confirmed", "Deaths", "Recovered"]
case_options = st.multiselect("Select case types:", case_types, case_types)

# TODO: slider for death, group by month ?

# TODO: make the x axis a date that displays year
st.line_chart(df.loc[df["Country"] == country_choice][case_options])

if st.checkbox("Raw Data"):
    st.subheader("Raw Data")
    st.write(df)