import streamlit as st
import time

# Set page title and layout
st.set_page_config(page_title="Countdown Timer", layout="centered")

# Custom CSS for dark theme and card design
st.markdown("""
    <style>
    /* Global styles */
    body {
        background-color: black !important;
        
    }
</style>
""", unsafe_allow_html=True)

# Define a function to format time in mm:ss format
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

# Title of the app with bright color
st.markdown("<h1 style='color: blue'>🐍 Learn Python 🐍</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='color: #FF5733;'>⏳ Countdown Timer ⏳</h1>", unsafe_allow_html=True)

# Display input label with yellow text
st.markdown("<h3 style='color: #00CC99;'>Enter duration in seconds:</h3>", unsafe_allow_html=True)

# Input for duration in seconds
duration = st.number_input(
    "",
    min_value=1, step=1, value=60,
    format="%d", help="Set the timer duration",
    key="duration"
)

# Initialize session state for timer
if 'time_left' not in st.session_state:
    st.session_state.time_left = 0
if 'is_active' not in st.session_state:
    st.session_state.is_active = False
if 'is_paused' not in st.session_state:
    st.session_state.is_paused = False

# Buttons for setting, starting, pausing, and resetting the timer
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Set", key="set_button"):
        st.session_state.time_left = duration
        st.session_state.is_active = False
        st.session_state.is_paused = False

with col2:
    if st.button("Start", key="start_button") and st.session_state.time_left > 0:
        st.session_state.is_active = True
        st.session_state.is_paused = False

with col3:
    if st.button("Pause", key="pause_button") and st.session_state.is_active:
        st.session_state.is_paused = True
        st.session_state.is_active = False

with col4:
    if st.button("Reset", key="reset_button"):
        st.session_state.is_active = False
        st.session_state.is_paused = False
        st.session_state.time_left = duration

# Create a placeholder for the timer
timer_placeholder = st.empty()

# Countdown logic with continuous update
if st.session_state.is_active and not st.session_state.is_paused:
    while st.session_state.time_left > 0:
        st.session_state.time_left -= 1
        timer_placeholder.markdown(
            f"<h2 style='color: #FF5733;'>🕒 Time Left: 🕒 {format_time(st.session_state.time_left)}</h2>",
            unsafe_allow_html=True
        )
        time.sleep(1)
        st.query_params["reload"] = "true"  # Force a reload to update the timer

    # Handle timer end
    st.session_state.is_active = False
    st.session_state.is_paused = False
    timer_placeholder.markdown(
        "<h2 style='color: #32CD32;'>🎉 Time's up!</h2>",
        unsafe_allow_html=True
    )
    st.balloons()  # Display balloons when the timer ends

# Display remaining time if timer is not active
if not st.session_state.is_active:
    timer_placeholder.markdown(
        f"<h2 style='color: blue;'>🕒 Time Left: 🕒 {format_time(st.session_state.time_left)}</h2>",
        unsafe_allow_html=True
    )

# Author information with 5 different bright colors
author_name = "<p style='text-align: center;'><b>" \
            "<span style='color: #FF4500;'>A</span>" \
            "<span style='color: #FF69B4;'>z</span>" \
            "<span style='color: #FFD700;'>m</span>" \
            "<span style='color: #7CFC00;'>a</span>" \
            "<span style='color: #1E90FF;'>t</span>" \
            " <span style='color: #FF4500;'>A</span>" \
            "<span style='color: #FF69B4;'>l</span>" \
            "<span style='color: #FFD700;'>i</span></b></p>"
st.markdown("---")
st.markdown(author_name, unsafe_allow_html=True)

