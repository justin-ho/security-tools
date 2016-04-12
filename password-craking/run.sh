#!/bin/bash

#  HAWAIIAN DICTIONARY
python gen-dictionary.py -u "http://hawaiian-words.com/hawaiian-dictionary" -o "hawaiian.dic" -s "<tr><td >" -e "</td>"

#  POSIX LIBRARY HEADERS
#python gen-dictionary.py -u "http://pubs.opengroup.org/onlinepubs/007908799/headix.html" -o "POSIX-lib.dic" -s ".html\">" -e "</A>"

#  ELEMENTS
#python gen-dictionary.py -u "https://www.webelements.com/" -o "elements.dic" -s "</div><div class=\"symbol\"><a class=\"sym\" href=\"" -e "/\">"
