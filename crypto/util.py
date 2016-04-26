#!/usr/bin/python

import sys
from substitution import vigenere


def mquit(message):
    """prints the given error message and then quits the program"""
    print message
    sys.exit(2)


def enumerate_vigenere(message, filename, encrypt):
    """Enumerates the filename performing a vigenere shift on each line of the file"""
    file = open(filename, 'r')
    iter = 0
    user = ''
    viewnumber = 10
    while iter != viewnumber or user != 'q':
        temp = file.readline().rstrip()
        if temp == '':
            break
        print vigenere(message, temp, encrypt)
        iter += 1
        if iter == viewnumber:
            user = raw_input('Press Enter to continue or q to quit: ')
            if user != 'q':
                iter = 0
    file.close()
