import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

# Step 1: Connect to Google Sheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open your Google Sheet by name
sheet = client.open("Mandir Algo Sheet").sheet1

# Step 2: Read data
data = sheet.get_all_records()

# Step 3: Apply logic and prepare updates
updated_rows = []
for i, row in enumerate(data):
    try:
        rsi = float(row.get("RSI", 0))
        signal = "Hold"
        if rsi > 70:
            signal = "Sell"
        elif rsi < 30:
            signal = "Buy"
        
        # Update the row in Google Sheet (assuming "Action" is in column H or 8th column)
        sheet.update_cell(i + 2, 8, signal)
        print(f"{row['Symbol']} - RSI: {rsi} => Signal: {signal}")
    except Exception as e:
        print(f"Error processing row {i + 2}: {e}")

# Step 4: Final message
print("Algo signals updated at", datetime.datetime.now())








