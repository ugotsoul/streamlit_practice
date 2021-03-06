"""
Plot airline passengers over time.
Complete each TODO to create a working streamlit app.
"""

import streamlit as st
import pandas as pd


# TODO: Add a title for the web app
st.title("International flight passenger data")

# TODO: Add a short text description what the web app does
st.text("Plot the total number of airline passengers by number of months")

# Load data is done for you
url = "https://raw.githubusercontent.com/brianspiering/datasets/main/airline_passenger_data.csv"
df = pd.read_csv(url)

# sidebar controls
st.sidebar.markdown("# Controls")

# TODO: Create sliders for start index and number of months
start_index = st.sidebar.slider('Start index', min_value=0, max_value=df.shape[0], step=1)
n_months  = st.sidebar.slider("Number of months", min_value=2, max_value=df.shape[0]-start_index, step=1)

# Select just the rows and single column to plot
data = df.iloc[start_index:start_index+n_months, 2]

# TODO: Create a line chart of the data
st.line_chart(data)