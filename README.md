# Google Drive File Lister

## Overview
This Python script provides a comprehensive solution for listing and categorizing files in a specific Google Drive project folder using the Google Drive API.

## Features
- Authenticate with Google Drive using service account credentials
- List files in a specified project folder
- Categorize files by type:
  - Videos
  - Documents
  - Spreadsheets
  - Presentations
- Robust error handling with detailed logging

## Prerequisites
- Python 3.x
- Google Cloud Project
- Google Drive API enabled
- Service Account Credentials

## Installation
1. Clone the repository
2. Install required dependencies:
   ```
   pip install google-auth google-auth-oauthlib google-api-python-client
   ```

## Configuration
- Replace `/path/to/service-account-key.json` with your service account key path
- Replace `FOLDER_ID_HERE` with your target Google Drive folder ID

## Usage
Run the script directly:
```
python google_drive_file_lister.py
```

## Error Handling
The script includes comprehensive error handling:
- Catches and logs HTTP errors
- Handles unexpected exceptions
- Provides detailed error information

## License
MIT License