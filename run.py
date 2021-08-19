from functions import typing


def select_aircraft():
    """
    Lets the user select aircraft from the range of aircraft.
    This sets the total fuel, passengers and weights.
    """
    typing("Welcome to the Loadsheet Planner\n", 0.02)
    typing("Retrieving the database of Aircraft\n", 0.02)
    typing('                         |                         \n', 0.01)
    typing('                         |                         \n', 0.01)
    typing('                         |                         \n', 0.01)
    typing('                        /|\                        \n', 0.01)
    typing('                     .-`   `-.                     \n', 0.01)
    typing('             _______-  -----  -_______             \n', 0.01)
    typing('                    -         -                    \n', 0.01)
    typing(' \__________________:         :__________________/ \n', 0.01)
    typing("   '''.-^-.' '.-^-.''\       /''.-^-.' '.-^-.'''    \n", 0.01)
    typing("      '___'   '___'   ''---''    '___'   '___'       \n", 0.01)

    typing("You have 3 aircraft available to you:\n", 0.02)
    typing("a) Boeing 747-400\n", 0.02)
    typing("b) Embraer 190\n", 0.02)
    typing("c) Jetstream 41\n", 0.02)

    aircraft_type = input("Please select the aircraft, enter a, b or c: ")
    return aircraft_type

select_aircraft()