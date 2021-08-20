from functions import typing


def opening_text():
    """
    Displays the opening text. details what aircraft are available to select.
    """
    typing("        Welcome to the Loadsheet Planner\n", 0.02)
    typing("      Retrieving the database of Aircraft...\n", 0.02)
    print()
    typing('                         |                         \n', 0.01)
    typing('                         |                         \n', 0.01)
    typing('                         |                         \n', 0.01)
    typing('                        /|\                        \n', 0.01)
    typing('                     .-`   `-.                     \n', 0.01)
    typing('             _______-  -----  -_______             \n', 0.01)
    typing('                    -         -                    \n', 0.01)
    typing(' \__________________:    o    :__________________/ \n', 0.01)
    typing("   '''.-^-.' '.-^-.''\       /''.-^-.' '.-^-.'''    \n", 0.01)
    typing("      '___'   '___'   ''---''   '___'   '___'       \n", 0.01)
    print()
    typing("-----By Ewan Colquhoun - not for operational use-----\n", 0.01)
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
    def __init__(self, model, maxPax, maxFuel, emptyWeight, maxWeight):
        self.model = model
        self.maxPax = int(maxPax)
        self.maxFuel = int(maxFuel)
        self.emptyWeight = int(emptyWeight)
        self.maxWeight = int(maxWeight)


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
    """
    minFuel = round(0.05 * type.maxFuel)
    typing(f"The maximum fuel for the {type.model} is {type.maxFuel}kg\n", 0.02)
    typing(f"The minimum fuel is {minFuel}kg.\n", 0.02)
    fuel = input("Please enter the total fuel in kg. eg, 140000, 8000, 1200: ")

    try:
        if int(fuel) <= minFuel:
            print("-------------FUEL TOO LOW-----------------")
            print("-----PLEASE ENTER a VALID FUEL FIGURE-----")
            fuel_quantity(type)
        elif int(fuel) <= type.maxFuel:
            typing(f"{fuel}kg is valid and has been accepted.\n", 0.02)
            return fuel
        else:
            print("---------FUEL QUANTITY TOO HIGH-----------")
            print("-----PLEASE ENTER a VALID FUEL FIGURE-----")
            fuel_quantity(type)
    except ValueError as e:
        print(e)
        print()
        print("------Please enter fuel as a number------\n")
        print(f"Maximum {type.maxFuel}kg. Minimum {minFuel}kg.\n")
        print()
        fuel_quantity(type)


def main():
    """
    Runs the application on loading the browser.
    """
    # opening_text()
    aircraft = select_aircraft()
    fuel = fuel_quantity(aircraft)


jumbo = Aircraft('Boeing 747-400', '331', '170000', '183500', '396000')
ejet = Aircraft('Embraer 190', '98', '12900', '28000', '45990')
jetstream = Aircraft('Jetstream 41', '29', '2700', '6400', '10800')

main()
