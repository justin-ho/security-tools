#!/usr/bin/python

"""Python script to perform a caesar shift on a caesar cipher

Shifting works with everything but these characters: $!
This bug seems to be due to bash issues.

-m,
    the message to cipher
-n,
    the number of shifts to shift the cipher
-e,
    Encrypt the message
-d,
    Decrypt the message
-a,
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
    qmessage = 'caesar.py -m <message> -n <number of shifts> [-a -e -d]'
    try:
        opts, args = getopt.getopt(argv, "m:n:eda")
    except getopt.GetoptError:
        mquit(qmessage)

    # All options must be specified except for the enumeration option
    if len(opts) < 3:
        mquit(qmessage)

    message = ''
    shifts = ''
    enum = False
    encrypt = True

    #  get and set all the user defined options
    for opt, arg in opts:
        if opt == '-m':
            message = arg
        elif opt == '-a':
            enum = True
        elif opt == '-e':
            encrypt = True
        elif opt == '-d':
            encrypt = False
        elif opt == '-n':
            if not arg.isdigit():
                mquit(qmessage)
            shifts = int(arg)

    #  quit the script if the message is empty or if the number of shifts is empty and the enumeration option is not set
    if message == '' or (shifts == '' and not enum):
        mquit(qmessage)

    #  if the enumeration option is set, enumerate all possibilities
    #  else shift the message by the given number of shifts
    if enum:
        for shifts in range(0, 26, 1):
            print caesar(message, shifts, encrypt)
    else:
        print caesar(message, shifts, encrypt)

if __name__ == "__main__":
    main()
