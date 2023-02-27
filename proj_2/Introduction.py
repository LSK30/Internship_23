import streamlit as st
import time
import numpy as np
import pandas as pd
import plotly.express as px
from datetime import date



import datetime as dt
dt_India_aware = dt.datetime.now(dt.timezone(dt.timedelta(hours=5, minutes=30)))
dt_UTC_aware = dt.datetime.now(dt.timezone.utc)
max_len = len(max(['Indian Time'], key=len))
current_time = f"{dt_India_aware:%d-%b-%y %H:%M:%S}"

st.markdown(f"<h1 style='text-align: right; color: Navy;'><small>{current_time}<small></h1>", unsafe_allow_html=True)




st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://www.pngitem.com/pimgs/m/60-600976_transparent-background-world-map-hd-png-download.png");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True)
st.title(':red[The Fortune 500]')
c = st.container()
c.write(':black[The Fortune 500 is an annual list compiled and published by Fortune magazine that ranks 500 of the largest United States corporations by total revenue for their respective fiscal years. The list includes publicly held companies, along with privately held companies for which revenues are publicly available. The concept of the Fortune 500 was created by Edgar P. Smith, a Fortune editor, and the first list was published in 1955.]')
c.write(':black[The Fortune 1000 is the extended version of The Fortune Global 500.]')
