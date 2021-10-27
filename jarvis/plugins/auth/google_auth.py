import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from .config import GoogleAuth


class GoogleAuth:
    """Handles Google API auth requests
    """    
    def __init__(self) -> None:
        self.scopes = GoogleAuth.scopes
        self.creds = None
        self.auth()
    
    def auth(self) -> None:
        """Google Auth
        The file token.json stores the user's access and refresh tokens, and is
        created automatically when the authorization flow completes for the first
        time.
        """
        if os.path.exists(GoogleAuth.token):
            self.creds = Credentials.from_authorized_user_file(GoogleAuth.token, self.scopes)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(GoogleAuth.creds, self.scopes)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(GoogleAuth.token, 'w') as token:
                token.write(self.creds.to_json())
