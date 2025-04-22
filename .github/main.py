
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/101_7UazH6bodfjSUY5LvweNetaq6T9UuBrp1isn4E1k/edit').sheet1

def fetch_and_update():
    data = sheet.get_all_records()
    for i, row in enumerate(data, start=2):  # start=2 to skip header
        symbol = row['Symbol']
        ltp = row['LTP']
        rsi = float(row['RSI'])
        ema = float(row['EMA'])
        oi = int(row['OI'])
        price_action = row['Price Action']

        # Simple logic
        if rsi < 30 and ltp > ema and 'bullish' in price_action.lower():
            signal = 'Buy'
        elif rsi > 70 and ltp < ema and 'bearish' in price_action.lower():
            signal = 'Sell'
        else:
            signal = 'Hold'

        sheet.update_cell(i, 7, signal)  # Final Signal
        sheet.update_cell(i, 8, signal)  # Action

if __name__ == "__main__":
    print("Algo system started at:", datetime.datetime.now())
    fetch_and_update()
