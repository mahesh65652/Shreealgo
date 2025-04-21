import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import time
import logging
from smartapi.smartConnect import SmartConnect  # SmartPython से सही import करें

# Google Sheets setup
def google_sheet_setup():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('sheet-access.json', scope)
    client = gspread.authorize(creds)
    return client.open_by_url('https://docs.google.com/spreadsheets/d/101_7UazH6bodfjSUY5LvweNetaq6T9UuBrp1isn4E1k/edit?usp=drivesdk').sheet1

# Function to get data from Google Sheets
def get_data_from_sheet():
    sheet = google_sheet_setup()
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

# Function to place order using SmartPython API
def place_order(symbol, qty, action):
    smart_api = SmartConnect(api_key="Your API Key", access_token="Your Access Token")  # API Key और Access Token जोड़ें
    
    # Order details
    order = smart_api.place_order(
        symbol=symbol,
        quantity=qty,
        action=action,
        productType="CASH",  # Modify as needed
        orderType="LIMIT",   # Modify as needed
        price=100            # Modify price as needed
    )
    return order

# Main Algo logic
def run_algo():
    df = get_data_from_sheet()  # Read data from Google Sheet
    
    # Process the signals in the dataframe
    for index, row in df.iterrows():
        symbol = row['Symbol']
        action = row['Action']
        qty = 1  # Define quantity as per your logic
        
        # If action is BUY or SELL, place order
        if action == "BUY" or action == "SELL":
            response = place_order(symbol, qty, action)
            print(f"Order placed for {symbol} with action {action}")
        
        time.sleep(1)  # Small delay to avoid hitting API rate limits

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run_algo()
