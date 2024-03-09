import streamlit as st
import pytz
from datetime import datetime
# Import the get_stock_price function from hello.py
from hello import get_stock_price
 
# Title of the web app
st.title('World Clock & Finance Data')
 
# Section for World Clock
st.header('World Clock')
 
# Dropdown menu for location selection
locations = pytz.all_timezones
selected_locations = st.multiselect('Select up to 4 locations:', locations, default=["UTC"])
 
# Display the time in the selected locations
for loc in selected_locations[:4]:  # Limit to up to 4 locations
    timezone = pytz.timezone(loc)
    loc_time = datetime.now(timezone)
    st.write(f"Time in {loc}: {loc_time.strftime('%Y-%m-%d %H:%M:%S')}")
 
# Finance Data Section
st.header('Finance Data')
 
# User input for stock symbol
user_symbol = st.text_input('Enter a stock symbol (e.g., AAPL for Apple):')
 
# Button to fetch stock price
if st.button('Get Stock Price'):
    if user_symbol:
        # Display stock price using the hello.py functionality
        stock_price = get_stock_price(user_symbol)
        st.write(stock_price)
    else:
        st.write("Please enter a stock symbol.")
 
# Bonus: UNIX Timestamp and Conversion
st.header('Bonus Features')
 
if st.checkbox('Show UNIX Timestamp'):
    st.write(f"Current UNIX Timestamp: {datetime.now().timestamp()}")
 
if st.checkbox('Convert UNIX Timestamp to Human Time'):
    unix_input = st.number_input('Enter UNIX Timestamp:', step=1.0, format="%f")
    if unix_input:
        human_time = datetime.fromtimestamp(unix_input)
        st.write(f"Human Time: {human_time.strftime('%Y-%m-%d %H:%M:%S')}")
