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
        st.write(f"UNIX timestamp: {unix_timestamp}")
        st.write(f"Convert UNIX timestamp to Human time: [Convert](https://example.com/convert?timestamp={unix_timestamp})")
        st.write("Real-time data:")
        st.write("- Finance: [Stock](https://example.com/finance/stock), [Forex](https://example.com/finance/forex), [Bitcoin](https://example.com/finance/bitcoin)")
        st.write("- Weather: [Current Weather](https://example.com/weather/current)")
        st.write("- 911 Calls: [Latest 911 Calls](https://example.com/911/latest)")
        
        
