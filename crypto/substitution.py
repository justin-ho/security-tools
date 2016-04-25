"""Functions for substitution ciphers"""

def shift(char, shifts):
    """Shifts the given character by the given number of shifts"""
    temp = ord(char) + (shifts % 26)
    #  if the shift reaches an edge, circle back around
    if not chr(temp).isalpha() or (char.isupper() and chr(temp).islower()):
        shifts = 26 - (shifts % 26)
        temp = ord(char) - shifts
    return chr(temp)


def vigenere(message, key):
    """performs a vigenere shift of the given message using the given key"""
    outstring = ''
    keyindex = 0
    temp = 0
    #  for each character in the input string if the character is a letter shift the character
    #  by the given number of shifts, given by the ascii value of the given key
    for index in range(len(message)):
        while not key[keyindex % len(key)].isalpha():
            keyindex += 1
        if message[index].isalpha():
            if key[keyindex % len(key)].islower():
                temp = ord(key[keyindex % len(key)]) - 97
            else:
                temp = ord(key[keyindex % len(key)]) - 65
            outstring += shift(message[index], temp)
            keyindex += 1
        else:
            outstring += message[index]
    return outstring


def caesar(message, numshifts):
    """performs a caesar shift of the given message using the given number of shifts"""
    outstring = ''
    #  for each character in the message if the character is a letter shift the character
    #  by the given number of shifts
    for c in message:
        if c.isalpha():
            outstring += shift(c, numshifts)
        else:
            outstring += c
    return outstring
