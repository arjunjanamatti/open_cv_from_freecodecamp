import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

# # SETTING PAGE CONFIG TO WIDE MODE
# st.beta_set_page_config(layout="wide")

# LOADING DATA
DATE_TIME = "date/time"
DATA_URL = (
    "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data

data = load_data(100000)
hour = st.slider(label='hour', min_value=0, max_value=23, value=12, step=1)
data = data[data[DATE_TIME].dt.hour == hour]

f'Map the geo data: {hour} hour'
st.map(data=data)

f'Raw data @ {hour}hour: ', data