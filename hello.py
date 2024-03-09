import requests
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
def get_stock_price(symbol):
   API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
   BASE_URL = 'https://www.alphavantage.co/query'
   params = {
       "function": "TIME_SERIES_DAILY",
       "symbol": symbol,
       "apikey": API_KEY
   }
   response = requests.get(BASE_URL, params=params)
   if response.status_code == 200:
       data = response.json()
       time_series = data.get('Time Series (Daily)')
       if time_series:
           latest_day = list(time_series.keys())[0]
           latest_data = time_series[latest_day]
           closing_price = latest_data['4. close']
           return f"The closing price of {symbol} on {latest_day} was: ${closing_price}"
       else:
           return "Data not found."
   else:
       return "Failed to fetch data."
# Example usage
if __name__ == "__main__":
   symbol = "AAPL"  # Example: Apple Inc.
   print(get_stock_price(symbol))