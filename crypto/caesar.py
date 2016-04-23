#!/usr/bin/python

"""Python script to perform a caesar shift on a caesar cipher

Shifting works with everything but these characters: $!
This bug seems to be due to bash issues.

-m,
    the message to cipher
-n,
    the number of shifts to shift the cipher
-e,
    Enumerate all 26 caesar shift possibilities

Example:
    python caesar.py -m 'This is my secret message' -n 8
"""


import sys
import getopt
from util import mquit
from substitution import caesar


def main():
    """Main function to run the script"""
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "m:n:e")
    except getopt.GetoptError:
        mquit('caesar.py -m <message> -n <number of shifts> [-e]')

    # All options must be specified except for the enumeration option
    if len(opts) < 2:
        mquit('caesar.py -m <message> -n <number of shifts> [-e]')

    message = ''
    shifts = ''
    enum = False

    #  get and set all the user defined options
    for opt, arg in opts:
        if opt == '-m':
            message = arg
        elif opt == '-e':
            enum = True
        elif opt == '-n':
            if not arg.isdigit():
                mquit('caesar.py -m <message> -n <number of shifts> [-e]')
            shifts = int(arg)

    #  quit the script if the message is empty or if the number of shifts is empty and the enumeration option is not set
    if message == '' or (shifts == '' and not enum):
        mquit('caesar.py -m <message> -n <number of shifts> [-e]')

    #  if the enumeration option is set, enumerate all possibilities
    #  else shift the message by the given number of shifts
    if enum:
        for shifts in range(0, 26, 1):
            print caesar(message, shifts)
    else:
        print caesar(message, shifts)

if __name__ == "__main__":
    main()
