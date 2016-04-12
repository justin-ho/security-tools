#!/usr/bin/python

import sys
import getopt
from caesar import shift

def main():
  argv = sys.argv[1:]

  try:
    opts, args = getopt.getopt(argv, "i:k:")
  except getopt.GetoptError:
    print 'vigenere.py -i <input string> -k <key to use for shifting>'
    sys.exit(2)

  #  All options must be specified
  if (len(opts) < 2):
    print 'vigenere.py -i <input string> -k <key to use for shifting>'
    sys.exit(2)

  #  get and set all the user defined options
  for opt, arg in opts:
    if (opt == '-i'):
      instring = arg
    elif (opt == '-k'):
      key = arg

  outstring = ""
  #  for each character in the input string if the character is a letter shift the character
  #  by the given number of shifts, given by the ascii value of the given key
  for index in range(len(instring)):
    if (instring[index].isalpha()):
      outstring += shift(instring[index], ord(key[index % len(key)])) 
    else:
      outstring += instring[index]
  print outstring

if (__name__ == "__main__"):
  main()
