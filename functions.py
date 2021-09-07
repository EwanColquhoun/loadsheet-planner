import sys
import time
import datetime
import gspread
from google.oauth2.service_account import Credentials

now = datetime.datetime.now()


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


"""
# http://www.fpdf.org/ Library - My template for the loadsheet creation.
def output_pdf(aircraft, adults, children):

    Uses FPDF to create a pdf of the loadsheet.

    zfw = (int(aircraft.eWeight)
           + int(aircraft.traffic_load)
           + int(aircraft.cargo))
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_xy(0, 30)
    pdf.set_font('helvetica', 'B', 14,)
    pdf.cell(60)
    pdf.cell(75, 30, f'LOADSHEET for {aircraft.model} on '
             f'{now.strftime("%Y-%m-%d")} at '
             f'{now.strftime("%H:%M:%S")}', 0, 2, 'C')
    pdf.cell(-40)
    # Passengers
    pdf.cell(60, 10, 'Passengers:', 0, 0, 'L')
    pdf.cell(60, 10, f'{adults} Adult, {children} Children', 'B', 2, 'L')
    pdf.cell(-60)
    # Basic Weight
    pdf.cell(60, 10, 'Basic Weight:', 0, 0, 'L')
    pdf.cell(40, 10, f'{aircraft.eWeight}kg', 'B', 2, 'L')
    pdf.cell(-60)
    # Traffic Load
    pdf.cell(60, 10, 'Traffic Load: ', 0, 0, 'L')
    pdf.cell(40, 10, f'{aircraft.traffic_load}kg', 'B', 2, 'L')
    pdf.cell(-60)
    # Cargo
    pdf.cell(60, 10, 'Cargo:', 0, 0, 'L')
    pdf.cell(40, 10, f'{aircraft.cargo}kg', 'B', 0, 'L')
    pdf.cell(40, 10, f'MAX: {int(aircraft.mtow) - int(aircraft.tow)}'
             f'kg', 'B', 2, 'L')
    pdf.cell(-100)
    # ZFW
    pdf.cell(60, 10, 'ZFW (zero fuel weight):', 0, 0, 'L')
    pdf.cell(40, 10, f'{zfw}kg', 'B', 2, 'L')
    pdf.cell(-60)
    # Fuel
    pdf.cell(60, 10, 'Fuel in Tanks:', 0, 0, 'L')
    pdf.cell(40, 10, f'{aircraft.fuel}kg', 'B', 0, 'L')
    pdf.cell(40, 10, f'MAX: {aircraft.maxFuel}', 'B', 2, 'L')
    pdf.cell(-100)
    # TOW
    pdf.cell(60, 10, 'TOW (take-off weight):', 0, 0, 'L')
    pdf.cell(40, 10, f'{aircraft.tow}kg', 'B', 2, 'L')
    pdf.cell(-60)
    # Underload
    pdf.cell(60, 10, 'Underload:', 0, 0, 'L')
    pdf.cell(40, 10, f'{int(aircraft.mtow) - int(aircraft.tow)}'
                     f'kg', 'B', 2, 'L')
    pdf.cell(-60)
    # Max
    pdf.cell(60, 10, 'Maximum is:', 0, 0, 'L')
    pdf.cell(40, 10, f'{aircraft.mtow}kg', 'B', 2, 'L')
    pdf.cell(-60)
    # Dispatcher Signature
    pdf.cell(60, 20, 'Dispatcher Signature', 0, 0, 'L')
    pdf.cell(80, 20, '', 'B', 2, 'L')
    pdf.cell(-60)
    # Captain Signature
    pdf.cell(60, 20, 'Captain Signature', 0, 0, 'L')
    pdf.cell(80, 20, '', 'B', 2, 'L')
    pdf.cell(-60)
    pdf.output('loadsheet.pdf')
"""


# The initial part of this method was inspired by the code institute love sandwiches project.
def spreadsheet(aircraft, adults, children, underload):
    """
    Create the loadsheet by populating a google spreadsheet
    """
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
    flight.update('A1', (f'Loadsheet generated for {aircraft.model}'
                  f' on {now.strftime("%Y-%m-%d")} at {now.strftime("%H:%M:%S")}'))
    flight.update('B2', adults + ' Adults' + ', ' + children + ' Children')
    flight.update('B3', aircraft.eWeight)
    flight.update('B4', aircraft.traffic_load)
    flight.update('B5', aircraft.cargo)
    flight.update('B6', aircraft.zfw)
    flight.update('B7', aircraft.fuel)
    flight.update('E7', aircraft.maxFuel)
    flight.update('B8', aircraft.tow)
    flight.update('B10', aircraft.mtow)
