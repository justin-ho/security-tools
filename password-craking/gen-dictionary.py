#!/usr/bin/python

"""Python script to generate a dictionary given a url and starting and ending delimeters

-u,
    The url to parse the dictionary from

-o,
    The output file to save the dictionary in

-s,
    The starting delimiter which the element is surrounded by

-e,
    The ending delimiter which the element is surrounded by

Example:
    HAWAIIAN DICTIONARY
    python gen-dictionary.py -u "http://hawaiian-words.com/hawaiian-dictionary"
    -o "hawaiian.dic" -s "<tr    ><td >" -e "</td>"
"""

import sys
import getopt
import urllib
from util import mquit


def main():
    """Main function to run the script"""
    argv = sys.argv[1:]
    qmessage = 'gen-dictionary.py -u <URL> -o <outputfile> -s <starting delimeter> -e <ending delimeter>'
    try:
        opts, args = getopt.getopt(argv, "u:o:s:e:")
    except getopt.GetoptError:
        mquit(qmessage)

    #  All options must be specified
    if len(opts) < 4:
        mquit(qmessage)

    url = ''
    output = ''
    start = ''
    end = ''
    #  get and set all the user defined options
    for opt, arg in opts:
        if opt == '-u':
            url = arg
        elif opt == '-o':
            output = arg
        elif opt == '-s':
            start = arg
        elif opt == '-e':
            end = arg

    #  require all options, if not exit
    if url == '' or output == '' or start == '' or end == '':
        mquit(qmessage)

    print "Openning output file: " + output
    outputfile = open(output, "w")
    print "Connecting to: " + url
    site = urllib.urlopen(url)

    #  Begin parsing
    #  if the line contains the start delimeter and the end delimeter take what's between the delimeters
    print "Parsing..."
    line = site.readline()
    while line != "":
        if line.find(start) != -1 and line.find(end) != -1:
            outputfile.write(line[line.find(start) + len(start): line.find(end)].rstrip() + "\n")
        line = site.readline()

    #  close connections
    print "Disconnecting from: " + url
    site.close()
    print "Closing output file: " + output
    outputfile.close()

if __name__ == "__main__":
    main()
