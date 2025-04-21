import gspread
from google.oauth2.service_account import Credentials

# Define the scope
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from JSON file
creds = Credentials.from_service_account_file("credentials.json", scopes=scope)

# Authorize with gspread
client = gspread.authorize(creds)

# Open your Google Sheet by name
sheet = client.open("YOUR_SHEET_NAME").sheet1

# Read and print first row (example)
row = sheet.row_values(1)
print("First row:", row)









