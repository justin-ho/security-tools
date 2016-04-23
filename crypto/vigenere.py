#!/usr/bin/python

"""Python script to decrypt a vigenere cipher

Uses the given key to shift the letters in the given message.

-m,
    The message to encrypt using the key

-k,
    The key to encrypt the message with

Example:
    python vigenere.py -m 'This is my secret message' -k 'mykey'
"""

import sys
import getopt
from substitution import vigenere
from util import mquit


def main():
    """Main function to run the script"""
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "m:k:")
    except getopt.GetoptError:
        mquit('vigenere.py -m <message> -k <key to use for shifting>')

    #  All options must be specified
    if len(opts) < 2:
        mquit('vigenere.py -m <message> -k <key to use for shifting>')

    #  get and set all the user defined options
    message = ''
    key = ''
    for opt, arg in opts:
        if opt == '-m':
            message = arg
        elif opt == '-k':
            key = arg

    #  quit if the user did not define a mandatory option
    if message == '' or key == '':
        mquit('vigenere.py -m <message> -k <key to use for shifting>')

    print vigenere(message, key)

if __name__ == "__main__":
    main()
