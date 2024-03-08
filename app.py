'''Change it into a world clock app
'''

import streamlit as st 
import datetime
import time
import pytz

st.title("World Clock")

# Time zones we want to display
time_zones = {
    "Los Angeles": "America/Los_Angeles",
    "New York": "America/New_York",
    "London": "Europe/London",
    "Moscow": "Europe/Moscow",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney"
}

placeholder = st.empty()

while True:
    with placeholder.container():
        # Display the current time for each time zone
        for city, tz in time_zones.items():
            now = datetime.datetime.now(pytz.timezone(tz))
            st.metric(city, now.strftime("%Y-%m-%d %H:%M:%S"))

    time.sleep(1)

