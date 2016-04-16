#!/bin/bash

#  **************** gen-dictionary.py Examples: **************************

#  HAWAIIAN DICTIONARY
python gen-dictionary.py -u "http://hawaiian-words.com/hawaiian-dictionary" -o "hawaiian.dic" -s "<tr><td >" -e "</td>"

#  POSIX LIBRARY HEADERS
python gen-dictionary.py -u "http://pubs.opengroup.org/onlinepubs/007908799/headix.html" -o "POSIX-lib.dic" -s ".html\">" -e "</A>"

#  ELEMENTS
python gen-dictionary.py -u "https://www.webelements.com/" -o "elements.dic" -s "</div><div class=\"symbol\"><a class=\"sym\" href=\"" -e "/\">"


#  ****************** hash-dictionary.py Examples: ***************************

#  HAWAIIAN DICTIONARY
python hash-dictionary.py -a sha512 -i "hawaiian.dic" -o "hashed-hawaiian.dic"

#  POSIX LIBRARY HEADERS
python hash-dictionary.py -a sha1 -i "POSIX-lib.dic" -o "hashed-POSIX.dic"

#  ELEMENTS
python hash-dictionary.py -a md5 -i "elements.dic" -o "hashed-elements.dic"

#  Flag generation example
python hash-dictionary.py -a sha256 -f "FLAG-" -i "hawaiian.dic" -o "flags.dic"
