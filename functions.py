# import time and sys module for typing effect function.
import sys
import time
from os import system, name


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
