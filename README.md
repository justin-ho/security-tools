# security-tools
A repository for security related tools

## password-cracking

### gen-dictionary.py
A tool to generate dictionaries from a given url for password cracking. The script will connect to the URL and parse for the starting and ending delimeters and take whatever is between the starting and ending delimeter and output it to the outputfile. 

To run the script execute this command:

```python gen-dictionary.py -u <URL> -o <outputfile> -s <starting delimeter> -e <ending delimeter>```
see run.sh for examples

### hash-dictionary.py
A tool to generate hashes from a dictionary. This tool was created to assist in creating password cracking challenges for CTF's. The tool will hash each line in the dictionary individually and output the hashes in hex to the outputfile. The option of specifying the hashing algorithm is given, if no hashing algorithm is specified the default algorithm is sha256.

To run the script execute this command: 

```python hash-dictionary.py [-a <hashing algorithm>] -i <input file> -o <output file>```

see run.sh for examples

## crypto

### caesar.py
A tool to perform a caesar shift on a given message with the given number of shifts. 

To run this script execute this command:

```python caesar.py -m <message> -n <number of shifts>```

### vigenere.py
A tool to perform a vigenere shift using the given message and the given key. 

To run this script execute this command: 

```python vigenere.py -m <message> -k <key>```
