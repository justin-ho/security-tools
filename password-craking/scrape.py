import urllib
import sys
import getopt
from util import mquit


def scrape(url, start, end):
    """Scrapes the given url using the given start and end delimiters

    :returns a list of the elements found
    """
    found = []
    print "Connecting to: " + url
    site = urllib.urlopen(url)

    #  Begin parsing
    #  if the line contains the start delimeter and the end delimeter take what's between the delimeters
    print "Parsing..."
    line = site.readline()
    while line != "":
        if line.find(start) != -1 and line.find(end) != -1:
            found.append(line[line.find(start) + len(start): line.find(end)])
        line = site.readline()

    # close connections
    print "Disconnecting from: " + url
    site.close()
    return found


def main():
    """Main function to run the script"""
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "u:o:s:e:")
    except getopt.GetoptError:
        mquit('scrape.py -u <URL> -o <outputfile> -s <starting delimiter> -e <ending delimiter>')

    # All options must be specified
    if len(opts) < 4:
        mquit('scrape.py -u <URL> -o <outputfile> -s <starting delimiter> -e <ending delimiter>')

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

    # require all options, if not exit
    if url == '' or output == '' or start == '' or end == '':
        mquit('scrape.py -u <URL> -o <outputfile> -s <starting delimiter> -e <ending delimiter>')

    print "Opening output file: " + output
    outputfile = open(output, "w")
    elements = scrape(url, start, end)
    for element in elements:
        outputfile.write(element + "\n")
    outputfile.close()


if __name__ == '__main__':
    main()
