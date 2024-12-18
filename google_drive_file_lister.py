import logging
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    creds = Credentials.from_authorized_user_file('/path/to/service-account-key.json', ['https://www.googleapis.com/auth/drive'])
    drive_service = build('drive', 'v3', credentials=creds)
    project_folder_id = 'FOLDER_ID_HERE'  # Replace with the actual folder ID
    query = f"'{project_folder_id}' in parents and trashed=false"
    fields = "files(id, name, mimeType)"
    results = drive_service.files().list(q=query, fields=fields).execute()
    files = results.get('files', [])
    
    videos = [f for f in files if f['mimeType'].startswith('video/')]
    documents = [f for f in files if f['mimeType'].startswith('application/vnd.google-apps.document')]
    spreadsheets = [f for f in files if f['mimeType'].startswith('application/vnd.google-apps.spreadsheet')]
    presentations = [f for f in files if f['mimeType'].startswith('application/vnd.google-apps.presentation')]
    
    logging.info(f"Videos ({len(videos)}):")   
    for video in videos:
        logging.info(f"- {video['name']} (ID: {video['id']})")   
    logging.info(f"\nDocuments ({len(documents)}):")   
    for doc in documents:
        logging.info(f"- {doc['name']} (ID: {doc['id']})")   
    logging.info(f"\nSpreadsheets ({len(spreadsheets)}):")   
    for sheet in spreadsheets:
        logging.info(f"- {sheet['name']} (ID: {sheet['id']})")   
    logging.info(f"\nPresentations ({len(presentations)}):")   
    for presentation in presentations:
        logging.info(f"- {presentation['name']} (ID: {presentation['id']})")   
except HttpError as error:
    logging.error(f'An error occurred: {error}')
    logging.error(f'HTTP error details: {error.content}')
except Exception as error:
    logging.error(f'An unexpected error occurred: {error}')