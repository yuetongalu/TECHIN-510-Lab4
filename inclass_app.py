import streamlit as st
import datetime
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

# Dropdown for selecting locations
selected_cities = st.multiselect("Select Locations", options=list(time_zones.keys()), default=["New York"], help="You can select up to 4 locations.")

# Limit selection to 4 locations
if len(selected_cities) > 4:
    st.error("You can select up to 4 locations.")
else:
    for city in selected_cities:
        tz = time_zones[city]
        now = datetime.datetime.now(pytz.timezone(tz))
        unix_timestamp = now.timestamp()
        st.metric(city, now.strftime("%Y-%m-%d %H:%M:%S"), f"UNIX: {unix_timestamp}")

# To update the time every second, you'll need to rerun the script every second.
# Streamlit does not natively support pushing updates to the frontend at a fixed interval (e.g., every second) without user interaction.
# Consider using JavaScript or another method for real-time updates in a production environment.

