from functions import typing


def opening_text():
    """
    Displays the opening text. details what aircraft are available to select.
    """
    typing("        Welcome to the Loadsheet Planner\n", 0.02)
    typing("   ....Retrieving the database of Aircraft....\n", 0.02)
    print()
    typing('                         |                         \n', 0.005)
    typing('                         |                         \n', 0.005)
    typing('                         |                         \n', 0.005)
    typing('                        /|\                        \n', 0.005)
    typing('                     .-`   `-.                     \n', 0.005)
    typing('             _______:  -----  :_______             \n', 0.005)
    typing('                    |         |                    \n', 0.005)
    typing(' \__________________:    o    :__________________/ \n', 0.005)
    typing("   '''.-^-.' '.-^-.''\       /''.-^-.' '.-^-.'''    \n", 0.005)
    typing("      '___'   '___'   ''---''   '___'   '___'       \n", 0.005)
    print()
    typing("-----By Ewan Colquhoun - not for operational use-----\n", 0.02)
    print()
    typing("You have 3 aircraft available to load:\n", 0.02)
    typing("a) Boeing 747-400\n", 0.02)
    typing("b) Embraer 190\n", 0.02)
    typing("c) Jetstream 41\n", 0.02)
    print()


class Aircraft:
    """
    Creates an instance of an Aircraft
    """
    def __init__(self, model, maxPax, pax, maxFuel, fuel, eWeight, mtow):
        self.model = model
        self.maxPax = maxPax
        self.pax = pax
        self.maxFuel = int(maxFuel)
        self.fuel = fuel
        self.eWeight = eWeight
        self.mtow = mtow


def select_aircraft():
    """
    Asks the user to input which aircraft they would like to load.
    if the input is invalid (not a,b or c) it returns an error and asks
    the user to try again.
    """
    aircraft_type = input("Please select the aircraft, enter a, b or c: ")

    if aircraft_type.lower() == 'a':
        aircraft_a = 'Boeing 747-400'
        print(f"You have chosen the {aircraft_a}\n")
        return jumbo
    elif aircraft_type.lower() == 'b':
        aircraft_b = 'Embraer 190'
        print(f"You have chosen the {aircraft_b}\n")
        return ejet
    elif aircraft_type.lower() == 'c':
        aircraft_c = 'Jetstream 41'
        print(f"You have chosen the {aircraft_c}\n")
        return jetstream
    else:
        print()
        print(f"-----You selected {aircraft_type}------")
        print("------That wasn't a valid aircraft------")
        print("Please select your aircraft from the options a, b or c.\n")
        select_aircraft()


def fuel_quantity(type):
    """
    Defines the maximum and minimum fuel quantities depending on which
    aircraft was selected by the user.
    Displays the maximum and minimum fuel values for the user. Once fuel is
    inputted the value is checked to ensure it is in the correct range.
    An error is thrown if the value isn't a whole number.
    """
    minFuel = round(0.05 * type.maxFuel)
    typing(f"The maximum fuel is {type.maxFuel}kg\n", 0.02)
    typing(f"The minimum fuel is {minFuel}kg.\n", 0.02)
    fuel = input("Please enter the total fuel in kg. eg, 140000, 8000, 1200: ")

    try:
        if int(fuel) <= minFuel:
            print()
            print("-------------FUEL TOO LOW-----------------")
            print("-----PLEASE ENTER A VALID FUEL FIGURE-----\n")
            fuel_quantity(type)
        elif int(fuel) <= type.maxFuel:
            typing(f"{fuel}kg is valid and has been accepted.\n", 0.02)
            return fuel
        else:
            print()
            print("---------FUEL QUANTITY TOO HIGH-----------")
            print("-----PLEASE ENTER A VALID FUEL FIGURE-----\n")
            fuel_quantity(type)
    except ValueError:
        print()
        print("-----PLEASE ENTER FUEL AS A WHOLE NUMBER-----\n")
        print(f"Maximum {type.maxFuel}kg. Minimum {minFuel}kg.\n")
        fuel_quantity(type)


def load_fuel(fuel, aircraft):
    """
    Uses the fuel figure from the fuel_quantity function to update the
    Aircraft.fuel of the aircraft in use.
    """
    if aircraft == jumbo:
        jumbo.fuel = fuel
        return
    elif aircraft == ejet:
        ejet.fuel = fuel
        return
    elif aircraft == jetstream:
        jetstream.fuel = fuel
        return


def main():
    """
    Runs the application on loading the browser.
    """
    # opening_text()
    aircraft = select_aircraft()
    fuel = fuel_quantity(aircraft)
    load_fuel(fuel, aircraft)
    pax = 4  # PAX here until load pax functino defined
    print(f"Total fuel loaded on {jumbo.model} is {jumbo.fuel}kg")
    # above print() is here until print ls function defined
    return pax  # PAX here until load pax functino defined


jumbo = Aircraft('Boeing 747-400', '331', '0', '170000',
                '0', '183500', '396000')
ejet = Aircraft('Embraer 190', '98', '0', '12900', '0', '28000', '45990')
jetstream = Aircraft('Jetstream 41', '29', '0', '2700', '0', '6400', '10800')

fleet = (jumbo, ejet, jetstream)
main()
