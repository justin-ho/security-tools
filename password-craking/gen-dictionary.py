#!/usr/bin/python

import sys
import getopt
import urllib

#  **************************** MAIN FUNCTION TO RUN THE SCRIPT *********************
def main():
  argv = sys.argv[1:]
  try:
    opts, args = getopt.getopt(argv, "u:o:s:e:")
  except getopt.GetoptError:
    print 'dictionary.py -u <URL> -o <outputfile> -s <starting delimeter> -e <ending delimeter>'
    sys.exit(2)

  #  All options must be specified
  if (len(opts) < 4):
    print 'dictionary.py -u <URL> -o <outputfile> -s <starting delimeter> -e <ending delimeter>'
    sys.exit(2)

  #  get and set all the user defined options
  for opt, arg in opts:
    if (opt == '-u'):
      url = arg
    elif (opt == '-o'):
      output = arg
    elif (opt == '-s'):
      start = arg
    elif (opt == '-e'):
      end = arg

  print "Openning output file: " + output
  outputfile = open(output, "w")
  print "Connecting to: " + url
  site = urllib.urlopen(url)

  #  Begin parsing 
  #  if the line contains the start delimeter and the end delimeter take what's between the delimeters
  print "Parsing..."
  line = site.readline()
  while (line != ""):
    if (line.find(start) != -1 and line.find(end) != -1):
      outputfile.write(line[line.find(start) + len(start) : line.find(end)] + "\n") 
    line = site.readline()

  #  close connections
  print "Disconnecting from: " + url
  site.close()
  print "Closing output file: " + output
  outputfile.close()

if __name__ == "__main__":
  main()

