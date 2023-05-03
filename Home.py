import streamlit as st
import time
from streamlit.components.v1 import html
from streamlit import components

st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout='wide')

load_page = st.empty()

with load_page.container():
    with open("index.html", encoding="utf8") as source:
        index_page = source.read()
    
    html(index_page, height=450)

placeholder = st.empty()
col1, col2 = st.columns(2)
with col1:
    st.empty()
with col2:
    clicked = placeholder.button("Click Me")
    
    
if clicked:
    placeholder.empty()
    load_page.empty()
    # Birthday page
    col1, col2 = st.columns(2)
    with col1:
        st.empty()
    with col2:
        placeholder = st.empty()
        with placeholder.container():
            N = 5
            readyin = False
            for sec in range(N, -1, -1):
                ss = sec % 60
                # st.write("Analysing your data please wait...")
                placeholder.metric("**Please wait...**", f"{ss:02d}")
                time.sleep(1)
        if ss == 0:
            #This would empty everything inside the container
            placeholder.empty()
            st.balloons()

    with open("birthday.html", encoding="utf8") as bday:
        loading_page = bday.read()
            
    html(loading_page, height=350)
    st.video("birthday_video.mp4")
    
    
    with open("wishes.html", encoding="utf8") as wish:
        wish_page = wish.read()
            
    html(wish_page, height=1450)
