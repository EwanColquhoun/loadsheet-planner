from functions import typing


def opening_text():
    """
    Displays the opening text. details what aircraft are available to select.
    """
    typing("Welcome to the Loadsheet Planner\n", 0.02)
    typing("Retrieving the database of Aircraft...\n", 0.02)
    print()
    typing('                         |                         \n', 0.01)
    typing('                         |                         \n', 0.01)
    typing('                         |                         \n', 0.01)
    typing('                        /|\                        \n', 0.01)
    typing('                     .-`   `-.                     \n', 0.01)
    typing('             _______-  -----  -_______             \n', 0.01)
    typing('                    -         -                    \n', 0.01)
    typing(' \__________________:         :__________________/ \n', 0.01)
    typing("   '''.-^-.' '.-^-.''\       /''.-^-.' '.-^-.'''    \n", 0.01)
    typing("      '___'   '___'   ''---''   '___'   '___'       \n", 0.01)
    print()
    typing("You have 3 aircraft available to load:\n", 0.02)
    typing("a) Boeing 747-400\n", 0.02)
    typing("b) Embraer 190\n", 0.02)
    typing("c) Jetstream 41\n", 0.02)
    print()


def select_aircraft():
    """
    Asks the user to input which aircraft they would like to load.
    if the input is invalid (not a,b or c) it returns an error and asks
    the user to try again.
    """
    aircraft_type = input("Please select the aircraft, enter a, b or c: ")

    if aircraft_type.lower() == 'a':
        aircraft_a = 'Boeing 747-400'
        print(f"You have chosen the {aircraft_a}")
        return aircraft_a
    elif aircraft_type.lower() == 'b':
        aircraft_b = 'Embraer 190'
        print(f"You have chosen the {aircraft_b}")
        return aircraft_b
    elif aircraft_type.lower() == 'c':
        aircraft_c = 'Jetstream 41'
        print(f"You have chosen the {aircraft_c}")
        return aircraft_c
    else:
        print()
        print(f"-----You selected {aircraft_type}------")
        print("------That wasn't a valid aircraft------")
        print("Please select your aircraft from the options a, b or c.\n")
        select_aircraft()


def main():
    """
    Runs the application on loading the browser.
    """
    opening_text()
    select_aircraft()


main()
aircraft = select_aircraft()
print(aircraft)