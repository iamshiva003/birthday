import streamlit as st
from streamlit.components.v1 import html
import time
from streamlit import components


st.set_page_config(page_title='My Project', page_icon=':tada:', layout='wide')
waiting = """
          <h1>Please Wait...
          """
col1, col2 = st.columns(2) 


# Starting the countdown
# with col1:
#     st.empty()
with col1:
    html(waiting)
    placeholder = st.empty()
    with placeholder.container():
        N = 5
        readyin = False
        for sec in range(N, -1, -1):
            ss = sec % 60
            # st.write("Analysing your data please wait...")
            placeholder.metric("**Surprise in...**", f"{ss:02d}")
            time.sleep(1)
    if ss == 0:
        #This would empty everything inside the container
        placeholder.empty()
        st.button("Click Me")
        st.balloons()
        st.header("Happy Birthday")

video = """
        <div class="container">
                <video controls autoplay="false">
                    <source src="birthday_video.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <!-- <div class="overlay">
                    <h2>Video Title</h2>
                    <p>Video description goes here</p>
                </div> -->
                
            </div>
        """
# html(video)

# video_file = open('birthday_video.mp4', 'rb')
# video_bytes = video_file.read()

# st.video(video_bytes, start_time=3)


video_url = "./birthday_video.mp4"
html(f'<video width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></video>', height=315)



# html_string = """
#                  <link rel="stylesheet" href="main.css">
#                  <h1>Happy Birthday</h1>
#                  <button>Click</button>
#                  <script>
#                     document.write("ok")
#                  </script>
#                 """
# style_string = """<style>
#                     body {
#                         background-color: rgb(215, 234, 250);
#                     }

#                     h1 {
#                         font-size: 50px;
#                         color: red;
#                         font-weight: bold;
#                         background-color: antiquewhite;
#                         border-radius: 10px;
#                         margin: 0;
#                         padding: 0;
#                     }
#                     button {
#                         margin: 15px;
#                         padding: 10px 15px;
#                         border-radius: 5px;
#                         background-color: blue;
#                         color: white;
#                     }
#                     button:hover {
#                         padding: 10px 15px;
#                         border-radius: 5px;
#                         background-color: white;
#                         color: blue;
#                         transition: 0.5ms;
#                     }
#                 </style>"""
# # st.markdown(html_string, unsafe_allow_html=True)

# final = html_string + style_string
# st.write("hi")
# html(final)
# st.balloons()
