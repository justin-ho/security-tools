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


def enumerate_vigenere(message, filename, encrypt):
    """Enumerates the filename file performing a vigenere shift
    on the message using each line from the file as the key"""
    fileobj = open(filename, 'r')
    iterator = 0
    user = ''
    viewnumber = 10
    #  print the enumeration 10 entries at a time
    while iterator != viewnumber or user != 'q':
        temp = fileobj.readline().rstrip()
        if temp == '':
            break
        print vigenere(message, temp, encrypt)
        iterator += 1
        #  When the enumeration pauses ask the user if they want to continue
        if iterator == viewnumber:
            user = raw_input('Press Enter to continue or q to quit: ')
            if user != 'q':
                iterator = 0
    fileobj.close()


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
