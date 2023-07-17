import pandas as pd
import streamlit as st
from streamlit_vizzu import Config, Data, VizzuChart

# Load the Zomato dataset
df = pd.read_csv("zomato_dataset.csv")

# Create a VizzuChart object
chart = VizzuChart()

# Add the dataset to the chart
data = Data()
data.add_data_frame(df)
chart.animate(data)

# Configure the chart
chart.animate(Config({"x": "Cuisine", "y": "Votes", "title": "Cuisine Popularity"}))

# Add the swap checkbox
if st.checkbox("Swap"):
    chart.animate(Config({"y": "Cuisine", "x": "Votes", "title": "Votes Distribution"}))

# Show the chart in the app
chart.show()
