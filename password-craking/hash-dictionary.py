#!/usr/bin/python

#  python script to hash every single line in a dictionary [input] file
#  can be used to create passwork cracking challenges for a CTF

import sys 
import getopt
import hashlib

#  quit the program and print the message, prints a default message if no message is given
def quit(message):
  if (message == ''):
    print 'Usage: hash-dictionary.py [-a <hashing algorithm>] -i <input file> -o <output file>'
  else:
    print message
  sys.exit(2)

#  main function to run the script
def main():
  argv = sys.argv[1:]
  try:
    opts, args = getopt.getopt(argv, "i:o:a:")
  except getopt.GetoptError:
    quit('')

  #  All options must be specified
  if (len(opts) < 2):
    quit('')

  inputfile = ''
  outputfile = ''
  algorithm = ''
  #  get and set all the user defined options
  for opt, arg in opts:
    if (opt == '-i'):
      inputfile = arg
    elif (opt == '-o'):
      outputfile = arg
    elif (opt == '-a'):
      algorithm = arg

  #  the input and output files must be set
  if (inputfile == '' or outputfile == ''):
     quit('')
 
  if (algorithm != '' and algorithm not in hashlib.algorithms_guaranteed):
    quit("Usage: \'" + algorithm + "\'" + " not a guaranteed algorithm")
    

  #  open input and output file objects
  print 'opening input file: ' + inputfile
  infile = open(inputfile, "r")
  print 'opening output file: ' + outputfile
  outfile = open(outputfile, "w")

  print 'hashing passwords...'
  #  for every line in the file
  for line in infile:
    #  set the hashing algorithm
    if (algorithm == ''):
      md = hashlib.sha256()
    else:
      md = hashlib.new(algorithm)
    #  set the hash message to the line from the input
    md.update(line.strip('\n'))
    #  write the hash to the output file
    outfile.write(md.hexdigest() + '\n')

  #  close out the file objects
  print 'closing input file: ' + inputfile
  outfile.close()
  print 'closing output file: ' + outputfile
  infile.close()

if __name__ == "__main__":
  main()
