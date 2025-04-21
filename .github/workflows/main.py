print("Algo Mandir Live")
print("Algo Mandir Live")
import pandas as pd
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator

# Google Sheet setup
SHEET_ID = 'YOUR_SHEET_ID_HERE'
SHEET_NAME = 'Sheet1'
CREDENTIALS_FILE = 'creds.json'  # Google Service Account JSON

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)

data = sheet.get_all_records()
df = pd.DataFrame(data)

# Mock Live Price Fetch (Replace with real-time API like Angel One or others)
def fetch_live_price(symbol):
    # For demo, return random number (Replace with actual API)
    return 200 + hash(symbol) % 50

# Indicators & Logic
def analyze_row(row):
    price = fetch_live_price(row['Symbol'])
    row['LTP'] = price

    close_prices = pd.Series([price - 2, price - 1, price])  # Dummy last 3 prices
    rsi = RSIIndicator(close=close_prices).rsi().iloc[-1]
    ema = EMAIndicator(close=close_prices, window=3).ema_indicator().iloc[-1]

    row['RSI'] = round(rsi, 2)
    row['EMA'] = round(ema, 2)
    row['OI'] = 1000 + hash(row['Symbol']) % 500  # Dummy OI
    row['Price Action'] = 'Above EMA' if price > ema else 'Below EMA'

    if rsi > 60 and price > ema:
        row['Final Signal'] = 'Buy'
    elif rsi < 40 and price < ema:
        row['Final Signal'] = 'Sell'
    else:
        row['Final Signal'] = 'Hold'
    
    row['Action'] = row['Final Signal']
    return row

# Apply to each row
updated_df = df.apply(analyze_row, axis=1)

# Update Sheet
sheet.update([updated_df.columns.values.tolist()] + updated_df.values.tolist())

print("Sheet updated successfully.")




