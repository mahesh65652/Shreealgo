import gspread
from google.oauth2.service_account import Credentials

# Define the scope
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Load credentials from JSON key file
creds = Credentials.from_service_account_file("credentials.json", scopes=scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet = client.open("Google_sheet").sheet1

# Example 1: Update A1 Cell
sheet.update('A1', 'Hello World')

# Example 2: Update B1 Cell
sheet.update('B1', 'Testing Update')

# Example 3: Update multiple cells at once
sheet.update('A2:B2', [['Buy', 'Sell']])

print("Sheet Updated Successfully!")
