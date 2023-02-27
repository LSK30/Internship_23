import streamlit as st
import os
from matplotlib import image
import pandas as pd

st.markdown('The Fortune 1000  Dataset Consist of Top 1000 ranked American Companies.')
c=st.container()

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Fortune_1000.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Fortune_1000.csv")


img = image.imread(IMAGE_PATH)

df = pd.read_csv(DATA_PATH)

c.subheader(f' 1. The data set consist of {df.shape[1]} columns and {df.shape[0]} rows.')

c.subheader(f'2. Features based on which the Ranks are decided :')
for i in df.columns:
    st.text(i)

n = len(df.select_dtypes('number').columns)
ca = len(df.select_dtypes('object').columns)
st.subheader(f'3. Number of Numerical Feature are {n} and Number of Categorical feature are {ca}')

st.subheader(f'4. Description of Numerical  Columns:')
st.dataframe(df.describe())


