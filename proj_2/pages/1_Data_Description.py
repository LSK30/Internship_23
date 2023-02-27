import streamlit as st
import os
from matplotlib import image
import pandas as pd
import io

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

sel = st.selectbox('Select the feature',['rank','profit','revenue','num. of employees','state','sector'])
if sel == 'rank':
    values = st.slider(
        'Select a range of Rank',
        0, 1000, (25, 75))
    dfi = df[(df[sel] <= values[1]) & (df[sel] >= values[0]) ]
elif sel == 'profit':
    values = st.slider(
        'Select a range of Profit',
        -6600.00, 95000.00, (25.00, 75.00))
    dfi = df[(df[sel] <= values[1]) & (df[sel] >= values[0]) ]
elif sel == 'revenue':
    values = st.slider(
        'Select a range of Revenue:',
        2100.00, 470000.00, (2100.00, 100000.00))
    dfi = df[(df[sel] <= values[1]) & (df[sel] >= values[0]) ]
elif sel == 'num. of employees':
    values = st.slider(
        'Select a range of Employees',
        100, 230000,(25, 75))
    dfi = df[(df[sel] <= values[1]) & (df[sel] >= values[0]) ]
elif sel == 'state':
    values= st.selectbox('Select a State' , df['state'].unique())
    dfi= df[df['state'] == values]
elif sel == 'sector':
    values= st.selectbox('Select a sector' , df['sector'].unique())
    dfi= df[df['sector'] == values]

st.dataframe(dfi)
st.header(":blue[Details of the Dataset]")

data_info = st.radio('select to view the Details of the Dataset:',
                      ('Head', 'Tail','Sample', 'Columns', 'Shape', 'Info', 'Descriptive Statistics'),
                      horizontal=True)

if data_info == 'Shape':
    st.write(f"Number of Rows:  {df.shape[0]}")
    st.write(f"Number of Columns:  {df.shape[1]}")
elif data_info == 'Head':
    st.write(f'The Head of the DataFrame:')
    st.write(df.head())
elif data_info == 'Tail':
    st.write(f'The tail of DataFrame : ')
    st.write(df.tail())
elif data_info == 'Sample':
    st.write(f'Randomd sample from DataFrame :')
    st.write(df.sample(10))  
elif data_info == 'Columns':
    dt = st.radio('select dtype' , ('number' , 'object'),horizontal=True)
    for column in list(df.select_dtypes(dt).columns):
        st.write(column)
elif data_info == 'Info':
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
else:
    st.write(df.describe())


