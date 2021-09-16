import sys
import time
import datetime
import gspread
from google.oauth2.service_account import Credentials

now = datetime.datetime.now()


# The variables below were inspired by the
# code institute love sandwiches project.
SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
        ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('loadsheet-planner')

flight = SHEET.worksheet('Current-Flight')


# Code Credit - Help with the typing() function was found here:
# https://stackoverflow.com/questions/4627033/printing-a-string-with-a-little-delay-between-the-chars
def typing(text, speed):
    """
    This is a modified print function,
    rather than the whole print statement appearing all at once,
    the text has a timing in-between characters. In turn, this
    provides a typing like animation.
    text = The text you wish to enter.
    speed = The typing animations speed.
    Currently not 100% functional in the CI template.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


def spreadsheet(flight, aircraft, adults, children, underload):
    """
    Create the loadsheet by populating a google spreadsheet.
    """
    flight.update('B1', (f'Loadsheet generated for {aircraft.model}'
                         f' on {now.strftime("%Y-%m-%d")}'
                         f' at {now.strftime("%H:%M:%S")}'))
    flight.update('C2', adults + ' Adults' + ', ' + children + ' Children')
    flight.update('C3', aircraft.eWeight)
    flight.update('C4', aircraft.traffic_load)
    flight.update('C5', aircraft.cargo)
    flight.update('C6', aircraft.zfw)
    flight.update('C7', aircraft.fuel)
    flight.update('F7', aircraft.maxFuel)
    flight.update('C8', aircraft.tow)
    flight.update('C10', aircraft.mtow)


def clearSpreadsheet(flight):
    """
    Clears the loadsheet after use.
    """
    flight.update('B1', (f'No aircraft loaded'
                         f' on {now.strftime("%Y-%m-%d")}'
                         f' at {now.strftime("%H:%M:%S")}'))
    flight.batch_clear(["C2:C8", "F7", "C10"])
