# import time and sys module for typing effect function.
import sys
import time
import os
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
    Currently not 100% functional in the CI template.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


# code from http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
def clear_terminal():
    """
    Clearing the terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


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

    pdf.set_font('arial', '', 12)
    pdf.close()
    pdf.output('loadsheet.pdf', 'F')
    pdf.output('loadsheeeet.pdf', 'D')
