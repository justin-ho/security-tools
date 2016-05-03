# security-tools
A repository for security related tools

## password-cracking

### gen-dictionary.py
A tool to generate dictionaries from a given url for password cracking. The script will connect to the URL and parse for the starting and ending delimeters and take whatever is between the starting and ending delimeter and output it to the outputfile. 

To run the script execute this command:

```python gen-dictionary.py -u <URL> -o <outputfile> -s <starting delimeter> -e <ending delimeter>```

see run.sh for examples

### hash-dictionary.py
A tool to generate hashes from a dictionary. This tool was created to assist in creating password cracking challenges for CTF's. The tool will hash each line in the dictionary individually and output the hashes in hex to the outputfile. The option of specifying the hashing algorithm is given, if no hashing algorithm is specified the default algorithm is sha256. if the flag option is used the hash will be concatenated to the given flag title.

To run the script execute this command: 

```python hash-dictionary.py [-a <hashing algorithm> -f <flag title>] -i <input file> -o <output file>```

see run.sh for examples

## crypto

### caesar.py
A tool to perform a caesar shift on a given message with the given number of shifts.

options:

-m,
    the message to cipher

-n,
    the number of shifts to shift the cipher

-e,
    Encrypt the message

-d,
    Decrypt the message

-a,
    Enumerate all 26 caesar shift possibilities

To run this script execute this command:

```python caesar.py -m <message> -n <number of shifts>```

### vigenere.py
A tool to perform a vigenere shift using the given message and the given key.

options:

-m,
    The message to encrypt using the key

-k,
    The key to encrypt the message with

-a,
    enumerate vigenere using keys in the dictionary

-f,
    dictionary file

-e,
    encrypt the message

-d,
    decrypt the message

To run this script execute this command: 

```python vigenere.py -m <message> -k <key> -e```

## stego

### office-steg.py
A tool to embed files in an office xml file at the longest path within the file
(files that end in x, eg .docx, .pptx, .xlsx, etc.).

options:

-c,
    The cover file to hide the embeded file in

-e,
    The file to embed in the cover file

-o,
    The name of the file to output to

To run this script execute this command:

```python office-steg.py -c <cover file name> -e <embed file name> -o <output file name>```