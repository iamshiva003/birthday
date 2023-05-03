import streamlit as st
from streamlit.components.v1 import html
import time
from streamlit import components

st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout='wide')







def index():
    with open("index.html") as source:
        index_page = source.read()
    
    placeholder.empty()
    html(index_page, height=700)

def birthday():
    # Loading HTML Files
    with open("birthday.html") as bday:
        loading_page = bday.read()
        
    placeholder.empty()
    html(loading_page, height=300)
    
    
placeholder = st.empty()
birthday()
st.button("Click", on_click=index)


# Starting the countdown
col1, col2 = st.columns(2) 
with col1:  
    st.empty()
    placeholder1 = st.empty() 
with col2:
    clicked = st.button("Click Me")
    
    if clicked:
        placeholder2 = st.empty()
        with placeholder2.container():
            N = 5
            readyin = False
            for sec in range(N, -1, -1):
                ss = sec % 60
                # st.write("Analysing your data please wait...")
                placeholder2.metric("**Analysing your data please wait...**", f"{ss:02d}")
                time.sleep(1)
        if ss == 0:
            #This would empty everything inside the container
            placeholder1.empty()
            placeholder2.empty()
            st.balloons()




# clicked = st.button("Click Me")
# ss = 0
# placeholder = st.empty()

# # Starting the countdown
# col1, col2 = st.columns(2) 
# with col1:  
#     st.empty()
# with col2:
#     if clicked:
#         with placeholder.container():
#             N = 5
#             readyin = False
#             for sec in range(N, -1, -1):
#                 ss = sec % 60
#                 # st.write("Analysing your data please wait...")
#                 placeholder.metric("**Analysing your data please wait...**", f"{ss:02d}")
#                 time.sleep(1)

# if ss == 0:
#     #This would empty everything inside the container
#     placeholder.empty()
#     st.balloons()
#     # html(index_page, height=350)
            