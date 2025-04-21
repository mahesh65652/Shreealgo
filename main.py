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

# Get all data from the sheet
data = sheet.get_all_values()

# Print the data
for row in data:
    print(row)
