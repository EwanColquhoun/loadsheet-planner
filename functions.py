# import time and sys module for typing effect function.
import sys
import time
from os import system, name
import datetime
from fpdf import FPDF

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
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
# End Code Credit


# https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    """
    When called it clears the interactive console.
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    else:  # for mac and linux(here, os.name is 'posix')
        _ = system('clear')


# http://www.fpdf.org/ used to output a PDF into the workspace.
def output_pdf(aircraft, adults, children):
    """
    Uses FPDF to create a pdf of the loadsheet.
    """
    zfw = (int(aircraft.eWeight)
           + int(aircraft.traffic_load)
           + int(aircraft.cargo))
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 30)
    pdf.set_font('arial', 'B', 14)
    pdf.cell(60)
    pdf.cell(75, 30, f'LOADSHEET for {aircraft.model} on '
                     f'{now.strftime("%Y-%m-%d")} at '
                     f'{now.strftime("%H:%M:%S")}', 0, 2, 'C')
    pdf.cell(-40)
    # Passengers
    pdf.cell(60, 10, 'Passengers:', 0, 0, 'L')
    pdf.cell(40, 10, f'{adults} Adult, {children} Children', 0, 2, 'L')
    pdf.cell(-60)
    # Basic Weight
    pdf.cell(60, 10, 'Basic Weight:', 0, 0, 'L')
    pdf.cell(40, 10, f'{aircraft.eWeight}kg', 0, 2, 'L')
    pdf.cell(-60)
    # Fuel
    pdf.cell(60, 10, 'Fuel in Tanks:', 0, 0, 'L')
    pdf.cell(40, 10, f'{aircraft.fuel}kg', 0, 0, 'L')
    pdf.cell(40, 10, f'MAX: {aircraft.maxFuel}', 0, 2, 'L')
    pdf.cell(-100)
    # Traffic Load
    pdf.cell(60, 10, 'Traffic Load: ', 0, 0, 'L')
    pdf.cell(40, 10, f'{aircraft.traffic_load}kg', 0, 0, 'L')
    pdf.cell(-100)
    # Cargo
    pdf.cell(60, 10, 'Cargo:', 0, 0, 'L')
    pdf.cell(40, 10, f'{aircraft.cargo}kg', 0, 0, 'L')
    pdf.cell(40, 10, f'MAX: {int(aircraft.mtow) - int(aircraft.tow)}'
                     f'kg', 0, 2, 'L')
    pdf.cell(-100)
    # Underload
    pdf.cell(60, 10, 'Underload:', 0, 0, 'L')
    pdf.cell(40, 10, f'{int(aircraft.mtow) - int(aircraft.tow)}kg', 0, 2, 'L')
    pdf.cell(-60)
    # ZFW
    pdf.cell(60, 10, 'ZFW (zero fuel weight):', 0, 0, 'L')
    pdf.cell(40, 10, f'{zfw}kg', 0, 2, 'L')
    pdf.cell(-60)
    # TOW
    pdf.cell(60, 10, 'TOW (take-off weight):', 0, 0, 'L')
    pdf.cell(40, 10, f'{aircraft.tow}kg', 0, 2, 'L')
    pdf.cell(-60)
    # Max
    pdf.cell(60, 10, 'Maximum is:', 0, 0, 'L')
    pdf.cell(40, 10, f'{aircraft.mtow}kg', 0, 2, 'L')
    pdf.cell(-60)

    pdf.set_font('arial', '', 12)
    pdf.output('loadsheet.pdf', 'F')
