#!/usr/bin/python

import sys
import getopt
from caesar import shift

def main():
  argv = sys.argv[1:]

  try:
    opts, args = getopt.getopt(argv, "m:k:")
  except getopt.GetoptError:
    print 'vigenere.py -m <message> -k <key to use for shifting>'
    sys.exit(2)

  #  All options must be specified
  if (len(opts) < 2):
    print 'vigenere.py -m <message> -k <key to use for shifting>'
    sys.exit(2)

  #  get and set all the user defined options
  message = ''
  key = ''
  for opt, arg in opts:
    if (opt == '-m'):
      message = arg
    elif (opt == '-k'):
      key = arg

  #  quit if the user did not define a mandatory option
  if (message == '' or key == ''):
    print 'vigenere.py -m <message> -k <key to use for shifting>'
    sys.exit(2)

  outstring = ""
  keyindex = 0
  temp = 0
  #  for each character in the input string if the character is a letter shift the character
  #  by the given number of shifts, given by the ascii value of the given key
  for index in range(len(message)):
    if (message[index].isalpha()):
      if (key[keyindex % len(key)].islower()):
        temp = ord(key[keyindex % len(key)]) - 97
      else:
        temp = ord(key[keyindex % len(key)]) - 65
      outstring += shift(message[index], temp) 
      keyindex += 1
    else:
      outstring += message[index]
  print outstring

if (__name__ == "__main__"):
  main()
