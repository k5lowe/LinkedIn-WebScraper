import os.path
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv


load_dotenv()
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

print(SPREADSHEET_ID)

RANGE_NAME = 'LinkedIn-WebScraper-Sheet!B4'

def authenticate_google_sheets():
    creds = None

    # Use token.pickle if it exists (stores credentials between runs)
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If no valid credentials available, initiate login flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',
                scopes=['https://www.googleapis.com/auth/spreadsheets'],
                redirect_uri='http://localhost:8080/'
            )
            
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('sheets', 'v4', credentials=creds)

def write_to_sheet(data):
    service = authenticate_google_sheets()
    body = {
        'values': data
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption='RAW',
        body=body
    ).execute()

    print(f"{result.get('updates').get('updatedCells')} cells updated.")


job_postings = [
    ["Title", "Company", "Location", "Link"],
    ["Software Engineer", "Google", "Toronto", "https://..."],
    ["Data Scientist", "Meta", "Remote", "https://..."]
]

write_to_sheet(job_postings)
