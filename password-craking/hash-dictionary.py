#!/usr/bin/python

#  python script to hash every single line in a dictionary [input] file
#  can be used to create password cracking challenges for a CTF
#  if flag option is set the hash will be concatenated to the flag title which can then be used as flags for a CTF

import sys
import getopt
import hashlib
from util import mquit


def main():
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "i:o:a:f:")
    except getopt.GetoptError:
        mquit('Usage: hash-dictionary.py [-a <hashing algorithm> -f <flag title>] -i <input file> -o <output file>')

    #  All options must be specified
    if len(opts) < 2:
        mquit('Usage: hash-dictionary.py [-a <hashing algorithm> -f <flag title>] -i <input file> -o <output file>')

    inputfile = ''
    outputfile = ''
    algorithm = ''
    flag = ''
    #  get and set all the user defined options
    for opt, arg in opts:
        if opt == '-i':
            inputfile = arg
        elif opt == '-o':
            outputfile = arg
        elif opt == '-a':
            algorithm = arg
        elif opt == '-f':
            flag = arg

    #  the input and output files must be set
    if inputfile == '' or outputfile == '':
        mquit('Usage: hash-dictionary.py [-a <hashing algorithm> -f <flag title>] -i <input file> -o <output file>')

    #  if an algorithm is given it must be a guaranteed algorithm
    if algorithm != '' and algorithm not in hashlib.algorithms_guaranteed:
        mquit("Usage: \'" + algorithm + "\'" + " not a guaranteed algorithm")

    #  open input and output file objects
    print 'opening input file: ' + inputfile
    infile = open(inputfile, "r")
    print 'opening output file: ' + outputfile
    outfile = open(outputfile, "w")

    print 'hashing input...'
    #  for every line in the file
    for line in infile:
        #  set the hashing algorithm
        if algorithm == '':
            md = hashlib.sha256()
        else:
            md = hashlib.new(algorithm)
        #  set the hash message to the line from the input
        md.update(line.strip('\n'))
        #  write the hash to the output file
        outfile.write(flag + md.hexdigest() + '\n')

    #  close out the file objects
    print 'closing input file: ' + inputfile
    outfile.close()
    print 'closing output file: ' + outputfile
    infile.close()

if __name__ == "__main__":
    main()
