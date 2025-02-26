import pandas as pd
import streamlit as st
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import os
import random
from st_clickable_images import clickable_images
import base64
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Positube",
    page_icon="👋",
)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("# Welcome to Positube! 👋")
st.sidebar.success("Select a demo below.")


# st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background: url("url_goes_here")
#     }
#    .sidebar .sidebar-content {
#         background: url("url_goes_here")
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )



def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('streamlit/background.png')

# Object notation
# st.sidebar.header("This is the header in the sidebar")


# "with" notation
# with st.sidebar:
    # st.header("This is the header")
    # st.subheader("This is the subheading")
    # st.write(10+20)
# st.header("Hello")


# Columns

# col1, col2 = st.columns(2)
# with col1:
#     st.text("Welcome")
#     st.subheader("Coding101withsteve")


# with col2:
#     st.text("Not welcome")



images = []
for file in ["streamlit/Final images/1.png",
             "streamlit/Final images/2.png",
             "streamlit/Final images/3.png",
             "streamlit/Final images/4.png"]:

    with open(file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        images.append(f"data:image/jpeg;base64,{encoded}")
clicked = clickable_images(
    images,
    titles=[f"Image #{str(i)}" for i in range(4)],
    div_style={"position": "relative", "display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "20px", "height": "200px"},
)
if clicked == 0:
    switch_page("About")
if clicked == 1:
    switch_page("Dashboard")
if clicked == 2:
     switch_page("Wordcloud")
if clicked == 3:
     switch_page("Top 1000")


st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")
