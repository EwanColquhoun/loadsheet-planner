from functions import typing, spreadsheet, clearSpreadsheet, flight
import datetime
import time

now = datetime.datetime.now()


def opening_text():
    """
    Displays the opening text. Displays what aircraft are available to select.
    """
    print("        Welcome to the Loadsheet Planner\n")
    print()
    typing("Retrieving the Aircraft database....\n", 0.02)
    print()
    typing('                         |                         \n', 0.005)
    typing('                         |                         \n', 0.005)
    typing('                         |                         \n', 0.005)
    typing('                        /|\\                        \n', 0.005)
    typing('                     .-`   `-.                     \n', 0.005)
    typing('             _______:  -----  :_______             \n', 0.005)
    typing('                    |         |                    \n', 0.005)
    typing(' \\__________________:    o    :__________________/ \n', 0.005)
    typing("   '''.-^-.' '.-^-.''\\       /''.-^-.' '.-^-.'''    \n", 0.005)
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
    Creates an instance of an Aircraft.
    """
    def __init__(self, model, maxPax, pax, traffic_load, maxFuel,
                 fuel, cargo, eWeight, zfw, tow, mtow):
        self.model = model
        self.maxPax = int(maxPax)
        self.pax = int(pax)
        self.traffic_load = int(traffic_load)
        self.maxFuel = int(maxFuel)
        self.fuel = int(fuel)
        self.cargo = int(cargo)
        self.eWeight = int(eWeight)
        self.tow = int(tow)
        self.mtow = int(mtow)
        self.zfw = int(zfw)


def select_aircraft():
    """
    Asks the user to input which aircraft they would like to load.
    If the input is invalid (not a,b or c) it returns an error and asks
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


def fuel_quantity(aircraft):
    """
    Defines the maximum and minimum fuel quantities depending on which
    aircraft was selected by the user.
    Displays the maximum and minimum fuel values for the user. Once fuel is
    inputted the value is checked to ensure it is in the correct range.
    It is then loaded onto the aircraft object instance.
    An error is thrown if the value isn't a whole number.
    """
    while True:
        typing("Fuel quantity...\n", 0.02)
        minFuel = round(0.02 * aircraft.maxFuel)
        typing(f"Current fuel load is {aircraft.fuel}kg.\n", 0.02)
        typing(f"The maximum fuel is {aircraft.maxFuel}kg\n", 0.02)
        typing(f"The minimum fuel is {minFuel}kg.\n", 0.02)
        fuel = input("Please enter the total fuel in kg. "
                     "eg, 140000, 8000, 1200: \n")

        try:
            if int(fuel) < minFuel:
                print()
                print("-------------FUEL TOO LOW-----------------")
                print("-----PLEASE ENTER A VALID FUEL FIGURE-----\n")
            elif int(fuel) <= aircraft.maxFuel:
                typing(f"{fuel}kg is valid and has been accepted.\n", 0.02)
                aircraft.fuel = fuel
                return fuel
            else:
                print()
                print("---------FUEL QUANTITY TOO HIGH-----------")
                print("-----PLEASE ENTER A VALID FUEL FIGURE-----\n")
        except ValueError:
            print()
            print("-----PLEASE ENTER FUEL AS A WHOLE NUMBER-----\n")
            print(f"Maximum {aircraft.maxFuel}kg. Minimum {minFuel}kg.\n")


def calculate_underload(aircraft):
    """
    Calculates the useful load to the user. This indicated how much additional
    weight the aircraft can carry. i.e passengers and cargo.
    """
    underload = int(aircraft.mtow) - int(aircraft.tow)
    return underload


def passenger_quantity(aircraft):
    """
    Defines the maximum quantity of passengers available to load.
    It asks for an input of passenger numbers.
    It checks for validity both in type and quantity and
    provides feedback to the user.
    """
    while True:
        print()
        typing("Passenger quantity...\n", 0.02)
        typing(f"Current passenger load is {aircraft.pax}\n", 0.02)
        typing(f"Maximum number of passengers is {aircraft.maxPax}.\n", 0.02)
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
            traffic_load = int(pax_weight) + int(bag_weight)

            if int(adult_pax) | int(child_pax) == '':
                print()
                print("-----PLEASE ENTER 0 IF NO PASSENGERS-----")
            elif int(adult_pax) + int(child_pax) > aircraft.maxPax:
                print()
                print("-----PASSENGER FIGURE TOO HIGH------")
                print(f"Max for the {aircraft.model} is "
                      f"{aircraft.maxPax} passengers.")
            else:
                typing(f"{pax} is valid and has been accepted.\n", 0.02)
                print(f"The passenger weight "
                      f"is {traffic_load}kg")
                return pax, traffic_load, adult_pax, child_pax
        except ValueError:
            print()
            print("-----PLEASE ENTER PASSENGERS AS A WHOLE NUMBER-----")


def load_passengers(aircraft, pax, traffic_load):
    """
    Adds passengers and traffic-load to the instance of Aircraft.
    """
    aircraft.pax = pax
    aircraft.traffic_load = traffic_load


def cargo_quantity(aircraft):
    """
    Asks for an input to represent the amount of cargo the user
    would like to carry.
    """
    while True:
        print()
        typing("Cargo quantity...\n", 0.02)
        typing(f"Current cargo load is {aircraft.cargo}kg.\n", 0.02)
        cargo_load = input("Please enter your requested"
                           " cargo load in kg, eg, 5500: \n")

        try:
            if cargo_load == '' or int(cargo_load) < 0:
                print()
                print("-----PLEASE ENTER 0 IF NO CARGO-----")
            else:
                typing(f"{cargo_load} is valid and has been accepted.\n", 0.02)
                aircraft.cargo = cargo_load
                return cargo_load
        except ValueError:
            print()
            print("-----PLEASE ENTER CARGO AS A WHOLE NUMBER-----\n")


def calculate_zfw(aircraft, traffic_load, cargo):
    """
    Calculate the weight of the aircraft with no fuel onboard.
    """
    zfw = (int(aircraft.eWeight) +
           int(aircraft.traffic_load) +
           int(aircraft.cargo))
    return zfw


def check_max_weight(aircraft, traffic_load, cargo, fuel, underload):
    """
    Performs a calculation to see if the take-off
    weight it acceptable.
    """

    while True:
        tow = (int(aircraft.eWeight) +
               int(aircraft.traffic_load) +
               int(aircraft.cargo) +
               int(aircraft.fuel))
        if tow > aircraft.mtow:
            print()
            typing(f"The take off weight is {tow}kg, "
                   f"maximum is {aircraft.mtow}kg\n", 0.02)
            print()
            print(f"----TAKE-OFF WEIGHT IS {abs(aircraft.mtow - tow)}"
                  f"kg ABOVE MAXIMUM----\n")
            typing("Please remove cargo, passengers or fuel:\n", 0.02)
            print("a) Cargo")
            print("b) Passengers")
            print("c) Fuel\n")
            choice = input("Please select a, b or c: \n")

            if choice.lower() == 'a':
                new_cargo = cargo_quantity(aircraft)
                aircraft.cargo = new_cargo
            elif choice.lower() == 'b':
                n_pax, n_traffic_load, _, _ = passenger_quantity(aircraft)
                aircraft.pax = n_pax
                aircraft.traffic_load = n_traffic_load
            elif choice.lower() == 'c':
                new_fuel = fuel_quantity(aircraft)
                aircraft.fuel = new_fuel
            else:
                return tow
        else:
            calculate_underload(aircraft)
            return tow


def print_loadsheet(aircraft, adults, children):
    """
    Function called once all inputs and data have been compiled and validated.
    Prints results.
    """
    zfw = (int(aircraft.eWeight) +
           int(aircraft.traffic_load) +
           int(aircraft.cargo))

    typing('Printing loadsheet......................\n', 0.01)
    time.sleep(1)
    print('.' * 40)
    time.sleep(1)
    print('.' * 40)
    time.sleep(1)
    print()
    print('-' * 78)
    print('-' * 78)
    print(f'Loadsheet generated for {aircraft.model}'
          f' on {now.strftime("%Y-%m-%d")} at {now.strftime("%H:%M:%S")}')
    print('-' * 78)
    print(f'Passengers:{adults} Adults\n'
          f'           {children} Children\n')
    print(f'Basic Weight:  {aircraft.eWeight}kg')
    print(f'Traffic Load:  {aircraft.traffic_load}kg')
    print(f'Cargo:         {aircraft.cargo}kg')
    print('-' * 78)
    print(f'ZFW:           {zfw}kg')
    print('-' * 78)
    print(f'Fuel in tanks: {aircraft.fuel}kg')
    print('-' * 78)
    print(f"TOW:           {aircraft.tow}kg ---- Underload:"
          f" {int(aircraft.mtow) - int(aircraft.tow)}kg")
    print('-' * 78)
    print(f"MTOW           {aircraft.mtow}kg")
    print('-' * 78)
    print('-' * 78)
    print('To view your loadsheet in printable format please click')
    print(' the "View loadsheet here" button below.')
    print()
    print('You may need to refresh the printed loadsheet tab.')
    print()


def another_flight():
    """
    Function gives the user to start the application again for another flight.
    """
    next_flight = input("Do you wish to load another flight? Y or N\n")
    if next_flight.lower() == 'y':
        main()
        return
    elif next_flight.lower() == 'n':
        time.sleep(1)
        print('Your flight has departed. '
              'Thank you for using Loadsheet Planner.\n')
        time.sleep(2)
        print('-' * 78)
        print('\nPlease click on the "Run Loadsheet Planner" '
              'button to begin\n')
        print('-' * 78)
        return
    else:
        print()
        print('Please enter Y to load another flight or'
              ' N to exit the application')
        print()
        another_flight()


def main():
    """
    Runs the application on loading the browser.
    """
    opening_text()
    clearSpreadsheet(flight)
    aircraft = select_aircraft()
    fuel = fuel_quantity(aircraft)
    pax, traffic_load, adults, children = passenger_quantity(aircraft)
    load_passengers(aircraft, pax, traffic_load)
    cargo = cargo_quantity(aircraft)
    underload = calculate_underload(aircraft)
    new_tow = check_max_weight(aircraft, traffic_load, cargo, fuel, underload)
    zfw = calculate_zfw(aircraft, traffic_load, cargo)
    aircraft.tow = new_tow
    aircraft.zfw = zfw
    print_loadsheet(aircraft, adults, children)
    spreadsheet(flight, aircraft, adults, children, underload)
    another_flight()


jumbo = Aircraft('Boeing 747-400', '331', '0', '0', '170000',
                 '0', '0', '183500', '183500', '183500', '396000')
ejet = Aircraft('Embraer 190', '98', '0', '0', '12900', '0',
                '0', '28000', '28000', '28000', '45990')
jetstream = Aircraft('Jetstream 41', '29', '0', '0', '2700',
                     '0', '0', '6400', '6400', '6400', '10800')

main()
