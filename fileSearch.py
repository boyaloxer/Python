#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="Search a document for lines containing a string.")
parser.add_argument('-f', '--file', dest='docProvided', metavar='example.txt', type=str, help='Provide a file to search thro>
parser.add_argument('-s', '--search', dest='varSearch', metavar='ExAmPlE', type=str, help='Enter a simple string to search f>
args = parser.parse_args()

try:
        doc = open(args.docProvided)
        str = args.varSearch
        for line in doc:
                if str.lower() in line:
                        print(line)
except Exception:
        print('Oops! There appears to be a problem with the file path you provided.')
