import datetime
from typing import Any, Optional
from googleapiclient.discovery import build
from jarvis.plugins.auth.google_auth import GoogleAuth
from .config import GoogleCalendar


class GoogleCalendar:
    def __init__(self, calendar_id: Optional[str] = None) -> None:
        self.calendars: dict = GoogleCalendar.calendars
        self.calendar_service: Any = build('calendar', 'v3', credentials=GoogleAuth().creds)
        self.current_calendar: dict = {calendar_id: self.calendars[calendar_id]} if calendar_id is not None else self.calendars
        self.events: dict = {}

    def list_events(self, min_time: Optional[str] = datetime.datetime.utcnow().isoformat() + 'Z', max_results: Optional[int] = 10) -> None:
        """Calendar API List Events
        """
        for index, cal in self.current_calendar.items():
            events_result = self.calendar_service.events().list(
                calendarId=cal, 
                timeMin=min_time, 
                maxResults=max_results, singleEvents=True, 
                orderBy='startTime').execute()
            tmp_events = events_result.get('items', [])
            self.events = self.events[index] = tmp_events
