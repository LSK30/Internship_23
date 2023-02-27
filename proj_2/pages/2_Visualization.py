import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Fortune_1000.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Fortune_1000.csv")


st.markdown(f"<h1 style='text-align: center; color:black;'><small>The Fortune 1000 Companies Data<small></h1>", unsafe_allow_html=True)


img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

company = st.selectbox("Select the Company:", df['company'].unique())
rank= int(df[df['company'] == company]['rank'])
st.markdown(f"<h1 style='text-align: center; color:red;'><small>Rank = {rank}<small></h1>", unsafe_allow_html=True)
fig_1 = px.bar(df[df['company'] == company], x=["profit","revenue"])
st.plotly_chart(fig_1, use_container_width=True)

state = st.selectbox("Select the state:" , df['state'].unique())
col1,col2 = st.columns(2)
fig_2 = px.bar(df[df['state'] == state], x="company",y="Market Cap")
col1.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.bar(df[df['state'] == state], x="company",y="num. of employees")
col2.plotly_chart(fig_3, use_container_width=True)