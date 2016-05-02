import sys
import getopt
import zipfile
import os.path
import random
from util import mquit


"""Python script to embed files in office xml files.

Cover file must be files that end in x, eg .docx, .pptx, .xlsx, etc.
These files use XML for their content which is leveraged in this script to hide files within the cover file.

-c,
    The cover file to hide the embeded file in

-e,
    The file to embed in the cover file

-o,
    The name of the file to output to"""


def main():
    """Main function to run the script"""
    argv = sys.argv[1:]
    qmessage = 'office-steg.py -c <cover file name> -e <embed file name> -o <output file name>'
    try:
        opts, args = getopt.getopt(argv, "c:e:o:")
    except getopt.GetoptError:
        mquit(qmessage)

    # All options must be specified except for the enumeration option
    if len(opts) < 3:
        mquit(qmessage)

    cfilename = ''
    efilename = ''
    ofilename = ''
    # get and set all the user defined options
    for opt, arg in opts:
        if opt == '-c':
            cfilename = arg
        elif opt == '-e':
            efilename = arg
        elif opt == '-o':
            ofilename = arg

    # validate user input
    if cfilename == '' or efilename == '' or ofilename == '':
        mquit(qmessage)
    if not os.path.isfile(cfilename):
        mquit(cfilename + ' : file does not exist')
    if not os.path.isfile(efilename):
        mquit(efilename + ' : file does not exist')
    if os.path.isfile(ofilename):
        mquit(ofilename + ' : cannot write to file, file already exists')

    # initialize required variables
    paths = []
    coverfile = zipfile.ZipFile(cfilename, 'r')
    outputfile = zipfile.ZipFile(ofilename, 'w')

    print 'Retrieving paths ...'
    for files in coverfile.namelist():
        # accumulate path's
        if files.find('/') != -1 and paths.count(files[:files.rfind('/') + 1]) == 0:
            paths.append(files[:files.rfind('/') + 1])
    # choose a random path to hide the file in
    pathindex = random.randrange(0, len(paths))
    print efilename + ' will be hidden here: ' + paths[pathindex]

    # string to add to [Content_Types].xml so that the file is not corrupted
    added = '<Override PartName=\"/' + paths[pathindex] + efilename + '\" ContentType=\"' \
            + paths[pathindex] + efilename + '\"/>'

    print 'Copying data from: ' + cfilename + ' to: ' + ofilename + ' ...'
    for files in coverfile.infolist():
        # copy all the files to the new archive except for the [Content_Types].xml file
        if files.filename != '[Content_Types].xml':
            content = coverfile.read(files.filename)
            outputfile.writestr(files, content)
        else:
            # append the added string to ensure the file does not become corrupted
            contenttypefile = coverfile.read(files.filename)
            outputfile.writestr(files, contenttypefile[:contenttypefile.find('</Types>')] + added + '</Types>')

    # embed the file in the new archive at the random path chosen
    print 'Inserting ' + efilename + ' ...'
    outputfile.write(efilename, paths[pathindex] + efilename)
    print 'Closing file streams ...'
    coverfile.close()
    outputfile.close()
    print efilename + ' hidden in : ' + paths[pathindex]

if __name__ == '__main__':
    main()
