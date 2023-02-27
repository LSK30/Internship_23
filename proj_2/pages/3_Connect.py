import streamlit as st
import os
from matplotlib import image
import matplotlib as plt

st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://img.freepik.com/free-vector/social-media-icons_53876-89125.jpg");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True)


st.title(':iphone: :blue[Connect]')
c=st.container()
c.header('Hi ,I hope you liked my work. You can connect with me on these Social Networks.')


st.markdown(
        f"""
        <a href="https://www.linkedin.com/in/landa-shasi-kumar-b40850259/">
            LINKEDIN
        </a>
        """,
        unsafe_allow_html=True)

st.markdown(
        f"""
        <a href="https://github.com/LSK30">
        GITHUB
        </a>
        """,
        unsafe_allow_html=True)

st.markdown(
        f"""
        <a href="http://discord.com/users/ShasiKumar#5059">
        DISCORD
        </a>
        """,
        unsafe_allow_html=True)

