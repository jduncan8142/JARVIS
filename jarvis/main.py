from plugins.auth.google_auth import GoogleAuth
from plugins.calendar.google_calendar import GoogleCalendar

g_auth = GoogleAuth()
g_cal = GoogleCalendar()

g_cal.list_events()
[print(str(i + " : " + x)) for i, x in g_cal.events.items()]
