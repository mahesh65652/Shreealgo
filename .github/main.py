
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Scope (Google Sheet access के लिए)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# JSON Key File (Json.key)
creds = ServiceAccountCredentials.from_json_keyfile_name('algosystem/Json.key', scope)

# Google Sheet Access
client = gspread.authorize(creds)

# Open Sheet (Your sheet name)
sheet = client.open("algosheet").worksheet("Sheet1")   # algosheet = Sheet name

# Sample data
sample_data = [
    ['NIFTY50', 22250, 65.3, 22180, 45000, 'Buy'],
    ['BANKNIFTY', 48000, 54.2, 47910, 32000, 'Hold'],
]

# Clear old data first (Row 2 se aage sab clear)
sheet.batch_clear(['A2:F1000'])

# Write new data
for i, row in enumerate(sample_data, start=2):
    sheet.update(f'A{i}:F{i}', [row])

print("Sheet updated successfully.")
