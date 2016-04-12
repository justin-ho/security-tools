#!/usr/bin/python

# shifting works with everything but these characters: $!
# this bug seems to be due to bash issues

import sys
import getopt

#  Shifts the given character by the given number of shifts
def shift(char, shifts):
  temp = ord(char) + (shifts % 26)
  #  if the shift reaches an edge, circle back around 
  if (not chr(temp).isalpha() or (char.isupper() and chr(temp).islower())):
    shifts = 26 - (shifts % 26)
    temp = ord(char) - shifts
  return chr(temp)

#  *************MAIN FUNCTION TO RUN THE SCRIPT *****************
def main():
  argv = sys.argv[1:]

  try:
    opts, args = getopt.getopt(argv, "m:n:")
  except getopt.GetoptError:
    print 'caesar.py -m <message> -n <number of shifts>'
    sys.exit(2)

  # All options must be specified
  if (len(opts) < 2):
    print 'caesar.py -m <message> -n <number of shifts>'
    sys.exit(2)

  message = ''
  shifts = ''
  #  get and set all the user defined options
  for opt, arg in opts:
    if (opt == '-m'):
      message = arg
    elif (opt == '-n'):
      if (not arg.isdigit()):
        print 'caesar.py -m <message> -n <number of shifts>'
        sys.exit(2)
      shifts = int(arg)
  if (message == '' or shifts == ''):
      print 'caesar.py -m <message> -n <number of shifts>'
      sys.exit(2)


  outstring = ""
  #  for each character in the message if the character is a letter shift the character
  #  by the given number of shifts
  for c in message:
    if (c.isalpha()):
      outstring += shift(c, shifts)
    else:
        outstring += c
  print outstring

if (__name__ == "__main__"):
  main()

