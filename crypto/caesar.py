#!/usr/bin/python

"""Python script to perform a caesar shift on a caesar cipher

Shifting works with everything but these characters: $!
This bug seems to be due to bash issues.

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
        opts, args = getopt.getopt(argv, "m:n:")
    except getopt.GetoptError:
        mquit('caesar.py -m <message> -n <number of shifts>')

    # All options must be specified
    if len(opts) < 2:
        mquit('caesar.py -m <message> -n <number of shifts>')

    message = ''
    shifts = ''
    #  get and set all the user defined options
    for opt, arg in opts:
        if opt == '-m':
            message = arg
        elif opt == '-n':
            if not arg.isdigit():
                mquit('caesar.py -m <message> -n <number of shifts>')
            shifts = int(arg)
    if message == '' or shifts == '':
        mquit('caesar.py -m <message> -n <number of shifts>')

    print caesar(message, shifts)

if __name__ == "__main__":
    main()
