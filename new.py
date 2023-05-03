import streamlit as st
from streamlit import components


# Set page title
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉")

# Page layout
st.write("""
# Happy Birthday! 🎂🎉
""")

# Add a name input field
name = st.text_input("Enter your name:")
if not name:
    st.warning("Please enter your name.")

# Add a date input field
date = st.date_input("Select your birthday:")
if not date:
    st.warning("Please select your birthday.")

# Calculate the age
today = st.button("Today's date")
if today:
    age = (st.date_session_state.date - date).days // 365
    st.write(f"You are {age} years old today, {name}!")

# Add some birthday decorations
st.balloons()
