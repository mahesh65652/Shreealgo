
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets connection
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Shree Algo Sheet").sheet1

# Fetch and update example
def fetch_and_update():
    data = sheet.get_all_records()
    print("Fetched Data:", data)

fetch_and_update()
