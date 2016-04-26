#!/usr/bin/python

"""Python script to decrypt a vigenere cipher

Uses the given key to shift the letters in the given message.

-m,
    The message to encrypt using the key

-k,
    The key to encrypt the message with

-a,
    enumerate vigenere using keys in the dictionary

-f,
    dictionary file

-e,
    encrypt the message

-d,
    decrypt the message

Example:
    python vigenere.py -m 'This is my secret message' -k 'mykey'
"""

import sys
import getopt
from substitution import vigenere
from util import mquit
from util import enumerate_vigenere


def main():
    """Main function to run the script"""
    argv = sys.argv[1:]
    qmessage = 'vigenere.py -m <message> -k <key to use for shifting> ' \
               '[-a -f -d -e]'

    try:
        opts, args = getopt.getopt(argv, "m:k:f:aed")
    except getopt.GetoptError:
        mquit(qmessage)

    #  All options must be specified
    if len(opts) < 2:
        mquit(qmessage)

    #  get and set all the user defined options
    message = ''
    key = ''
    dictionary = ''
    enum = False
    encrypt = True
    for opt, arg in opts:
        if opt == '-m':
            message = arg
        elif opt == '-k':
            key = arg
        elif opt == '-f':
            dictionary = arg
        elif opt == '-a':
            enum = True
        elif opt == '-e':
            encrypt = True
        elif opt == '-d':
            encrypt = False

    #  quit if the user did not define a mandatory option
    if message == '' or (not enum and key == '') or (enum and dictionary == ''):
        mquit(qmessage)

    if enum:
        enumerate_vigenere(message, dictionary, encrypt)
    else:
        print vigenere(message, key)

if __name__ == "__main__":
    main()
