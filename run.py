from functions import typing


def opening_text():
    """
    Displays the opening text. Displays what aircraft are available to select.
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
    maxPax = maximum passengers,
    pax = number of passengers,
    eWeight = empyt weight of the aircraft without fuel, cargo and pax,
    mtow = Maximum allowed take-off weight.
    """
    def __init__(self, model, maxPax, pax, maxFuel, fuel, cargo, eWeight, mtow):
        self.model = model
        self.maxPax = int(maxPax)
        self.pax = int(pax)
        self.maxFuel = int(maxFuel)
        self.fuel = int(fuel)
        self.cargo = int(cargo)
        self.eWeight = int(eWeight)
        self.mtow = int(mtow)


def select_aircraft():
    """
    Asks the user to input which aircraft they would like to load.
    if the input is invalid (not a,b or c) it returns an error and asks
    the user to try again.
    """
    while True:
        ac_type = input("Please select the aircraft, enter a, b or c: \n")
        if ac_type.lower() == 'a':
            aircraft_a = 'Boeing 747-400'
            print(f"You have chosen the {aircraft_a}\n")
            return jumbo
        elif ac_type.lower() == 'b':
            aircraft_b = 'Embraer 190'
            print(f"You have chosen the {aircraft_b}\n")
            return ejet
        elif ac_type.lower() == 'c':
            aircraft_c = 'Jetstream 41'
            print(f"You have chosen the {aircraft_c}\n")
            return jetstream
        else:
            print()
            print(f"-----You selected {ac_type}------")
            print("------That wasn't a valid aircraft------")
            print("Please select your aircraft from the options a, b or c.\n")

    return


def fuel_quantity(type):
    """
    Defines the maximum and minimum fuel quantities depending on which
    aircraft was selected by the user.
    Displays the maximum and minimum fuel values for the user. Once fuel is
    inputted the value is checked to ensure it is in the correct range.
    An error is thrown if the value isn't a whole number.
    """
    while True:
        typing("Fuel quantity...\n", 0.02)
        minFuel = round(0.05 * type.maxFuel)
        typing(f"The maximum fuel is {type.maxFuel}kg\n", 0.02)
        typing(f"The minimum fuel is {minFuel}kg.\n", 0.02)
        fuel = input("Please enter the total fuel in kg. "
                     "eg, 140000, 8000, 1200: \n")

        try:
            if int(fuel) <= minFuel:
                print()
                print("-------------FUEL TOO LOW-----------------")
                print("-----PLEASE ENTER A VALID FUEL FIGURE-----\n")
            elif int(fuel) <= type.maxFuel:
                typing(f"{fuel}kg is valid and has been accepted.\n", 0.02)
                return fuel
            else:
                print()
                print("---------FUEL QUANTITY TOO HIGH-----------")
                print("-----PLEASE ENTER A VALID FUEL FIGURE-----\n")
        except ValueError:
            print()
            print("-----PLEASE ENTER FUEL AS A WHOLE NUMBER-----\n")
            print(f"Maximum {type.maxFuel}kg. Minimum {minFuel}kg.\n")


def load_fuel(fuel, type):
    """
    Uses the fuel figure from the fuel_quantity function to update the
    Aircraft.fuel of the aircraft in use.
    """
    if type == jumbo:
        jumbo.fuel = fuel
        return
    elif type == ejet:
        ejet.fuel = fuel
        return
    elif type == jetstream:
        jetstream.fuel = fuel
        return


def calculate_underload(aircraft, fuel, pax_weight, bag_weight):
    """
    Calculates the useful load to the user. This indicated how much additional
    weight the aircraft can carry. i.e passengers and cargo.
    """
    underload = (int(aircraft.mtow)
        - int(aircraft.eWeight)
        - int(aircraft.fuel)
        - int(pax_weight)
        - int(bag_weight))

    typing(f"The underload before cargo is {underload}kg\n", 0.02)
    return underload


def passenger_quantity(type):
    """
    Defines the maximum quantity of passengers available to upload based on the
    underload the aircraft has. It asks for an input of passenger numbers.
    It checks for validity both in type and quantity and feedsback to the
    user if there are any errors or if they are successful with their input.
    """
    while True:
        print()
        typing("Passenger quantity...\n", 0.02)
        typing("Passenger weights are 86kg for "
            "adults and 35kg for children\n", 0.02)
        typing("Each passenger is assumed to "
            "have 15kg of hand luggage.\n", 0.02)
        adult_pax = input("Please enter the number of ADULT passengers: \n")
        child_pax = input("Please enter the number of CHILD passengers: \n")
        pax = ''
        pax_weight = ''
        bag_weight = ''

        try:
            pax = int(adult_pax) + int(child_pax)
            pax_weight = (int(adult_pax) * 86) + (int(child_pax) * 35)
            bag_weight = int(pax) * 15

            if int(adult_pax) | int(child_pax) == '':
                print()
                print("-----PLEASE ENTER 0 IF NO PASSENGERS-----")
            elif int(adult_pax) + int(child_pax) > type.maxPax:
                print()
                print("-----PASSENGER FIGURE TOO HIGH------")
                print(f"Max for the {type.model} is {type.maxPax} passengers.")
            else:
                typing(f"{pax} is valid and has been accepted.\n", 0.02)
                print(f"The passenger weight "
                     f"is {int(pax_weight) + int(bag_weight)}kg")
                print()
                return pax, pax_weight, bag_weight
        except ValueError:
            print()
            print("Please enter passenger figure as a whole number only.")


def load_passengers(type, pax):
    """
    Calculates the passenger weight then adds
    the number of passengers to the instance of Aircraft.
    """
    if type == jumbo:
        jumbo.pax = pax
        return
    elif type == ejet:
        ejet.pax = pax
        return
    elif type == jetstream:
        jetstream.pax = pax
        return


def cargo_quantity(underload):
    """
    Inputs the amount of cargo for the flight in kg. Validates the input.
    """
    while True:
        print()
        typing("Cargo quantity...\n", 0.02)
        typing("Cargo is loaded if you have any spare underload.\n", 0.02)
        typing(f"Your underload is {underload}kg.\n", 0.02)
        cargo_load = input("Please enter your cargo load in kg, eg, 5500: \n")
       
        try:
            
            if cargo_load == '':
                print()
                print("-----PLEASE ENTER 0 IF NO CARGO-----")
            elif int(cargo_load) > int(underload):
                print()
                print("-----CARGO QUANTITY TOO HIGH------")
                print(f"Max cargo is {underload}kg.")
            else:
                typing(f"{cargo_load} is valid and has been accepted.\n", 0.02)
                return cargo_load
        except ValueError:
            print()
            print("Please enter cargo figure as a whole number only.")


def load_cargo(type, cargo):
    """
    Loads the cargo onto the Aircraft class.
    """
    type.cargo = cargo
    print(f'the {type.model} has {type.cargo}kg of cargo')


def check_max_weight(type, weight, bags, cargo):
    """
    Performs a calculation to see if the aircrafts take-off
    weight it acceptable. Dependant on fuel and passenger load.
    """
    while True:
        tow = (int(type.eWeight)
        + int(weight)
        + int(bags)
        + int(cargo)
        + int(type.fuel))

        if tow > type.mtow:
            print()
            typing(f"The take off weight is {tow}kg, "
                f"maximum is {type.mtow}kg\n", 0.02)
            print("-----TAKE-OFF WEIGHT IS ABOVE MAXIMUM-----\n")
            typing("Please remove cargo, passengers or fuel:\n", 0.02)
            print("a) Cargo")
            print("b) Passengers")
            print("c) Fuel\n")
            choice = input("Please select a, b or c: \n")
            if choice.lower() == 'a':
                new_cargo = cargo_quantity(underload)
                type.cargo = new_cargo
                tow = (int(type.eWeight)
                    + int(weight)
                    + int(bags)
                    + int(cargo)
                    + int(type.fuel))
            elif choice.lower() == 'b':
                new_pax, pax_weight, bag_weight = passenger_quantity(type)
                type.pax = new_pax
                tow = (int(type.eWeight)
                    + int(new_pax)
                    + int(bags)
                    + int(cargo)
                    + int(type.fuel))
                return tow
            elif choice.lower() == 'c':
                new_fuel = fuel_quantity(type)
                type.fuel = new_fuel
                tow = (int(type.eWeight)
                    + int(new_pax)
                    + int(bags)
                    + int(cargo)
                    + int(type.fuel))
                return tow
            else:
                return
        else:
            return tow


def main():
    """
    Runs the application on loading the browser.
    """
    opening_text()
    aircraft = select_aircraft()
    fuel = fuel_quantity(aircraft)
    load_fuel(fuel, aircraft)
    pax, pax_weight, bag_weight = passenger_quantity(aircraft)
    load_passengers(aircraft, pax)
    underload = calculate_underload(aircraft, fuel, pax_weight, bag_weight)
    cargo = cargo_quantity(underload)
    load_cargo(aircraft, cargo)
    new_tow = check_max_weight(aircraft, pax_weight, bag_weight, cargo)

    print("BELOW IS FOR TEST ONLY and will be removed on final deployment")
    print(f"Total load on {aircraft.model} is {aircraft.fuel}kg")
    print(f"of fuel and {aircraft.pax} passengers.")
    print(f"The Take-off weight is {new_tow}kg")
    print(f"Maximum is {aircraft.mtow}kg - ({aircraft.mtow - new_tow}kg)")


jumbo = Aircraft('Boeing 747-400', '331', '0', '0', '170000', 
    '0', '183500', '396000')
ejet = Aircraft('Embraer 190', '98', '0', '12900', '0', '0', '28000', '45990')
jetstream = Aircraft('Jetstream 41', '29', '0', '2700', '0', '0', '6400', '10800')

fleet = (jumbo, ejet, jetstream)
main()
