#!/usr/bin/env python
import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186
def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)
#Welcome Message

welcome = """
 _    _      _                          
| |  | |    | |                         
| |  | | ___| | ___ ___  _ __ ___   ___ 
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ /
\  /\  /  __/ | (_| (_) | | | | | |  __/
 \/  \/ \___|_|\___\___/|_| |_| |_|\___/      

Welcome To Shining Dev's basic Python miles to kilometers converter.  
"""
r1 = "[*] Please use only numbers \n"

printout(welcome, RED)
printout(r1, GREEN)

# Ask the user to input a number of miles which would be stored as the variable "miles"

miles = input("Please input miles: ")

#Stores Miles as a float

miles = float(miles)

#Does the math

kilometers = miles / 0.62137

#Prints the kilometers

print("there are {} kilometers in {} miles.".format(kilometers, miles))