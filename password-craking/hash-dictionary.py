#!/usr/bin/python

"""Python script to hash every single line in a dictionary [input] file

Can be used to create password cracking challenges for a CTF.
If the flag option is set the hash will be concatenated to the flag title which can then be used as flags for a CTF.

-a,
    The hashing algorithm to use. Taken from hashlib.algorithms_guaranteed
    set(['sha1', 'sha224', 'sha384', 'sha256', 'sha512', 'md5'])

    **Note: Script can be edited to use hashlib.algorithms_available instead for more options
    set(['SHA1', 'SHA224', 'SHA', 'SHA384', 'ecdsa-with-SHA1', 'SHA256', 'SHA512', 'md4', 'md5', 'sha1', 'dsaWithSHA',
    'DSA-SHA', 'sha224', 'dsaEncryption', 'DSA', 'ripemd160', 'sha', 'MD5', 'MD4', 'sha384', 'sha256', 'sha512',
    'RIPEMD160', 'whirlpool'])

-f,
    The flag title. If this option is given the hash will be concatenated to the flag title which can then be used
    as flags for a Capture The Flag (CTF) scenario

-i,
    The input file/dictionary to hash. This is the unhashed messages which will be hashed by this script

-o,
    The output file to write the hashes to.

Example:
HAWAIIAN DICTIONARY
python hash-dictionary.py -a sha512 -i "hawaiian.dic" -o "hashed-hawaiian.dic"

"""

import sys
import getopt
import hashlib
from util import mquit


def main():
    """Main function to run the script"""
    argv = sys.argv[1:]
    qmessage = 'Usage: hash-dictionary.py [-a <hashing algorithm> -f <flag title>] -i <input file> -o <output file>'
    try:
        opts, args = getopt.getopt(argv, "i:o:a:f:")
    except getopt.GetoptError:
        mquit(qmessage)

    #  All options must be specified
    if len(opts) < 2:
        mquit(qmessage)

    inputfile = ''
    outputfile = ''
    algorithm = 'sha256'
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
        mquit(qmessage)

    #  if an algorithm is given it must be a guaranteed algorithm
    if algorithm != 'sha256' and algorithm not in hashlib.algorithms_guaranteed:
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
