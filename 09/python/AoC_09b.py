#!/usr/bin/env python3

import sys
import os.path
import re

garbagePattern = re.compile(r'<([^>]*)>')
ignorePattern = re.compile(r'!.')

def removeIgnored(data):
    return ignorePattern.sub('', data)

def countGarbage(data):
    return sum([len(m) for m in garbagePattern.findall(data)])

def main(data):
    data = removeIgnored(data)
    return countGarbage(data)

if __name__ == '__main__':
    testVectors = {
        '<>': 0,
        '<random characters>': 17,
        '<<<<>': 3,
        '<{!>}>': 2,
        '<!!>': 0,
        '<!!!>>': 0,
        '<{o"i!a,<{i<a>': 10,
    }
    
    testResults = [ main(ti) == tr for ti, tr in testVectors.items() ]
    if all(testResults):
        print("All tests passed!")
        inputFile = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(sys.argv[0])
                )
            ), 'input'
        )
        if os.path.isfile(inputFile):
            with open(inputFile, 'r') as fh:
                inputData = fh.read()
                inputData = inputData.strip()
            print(main(inputData))
        else:
            print("Input file not found")
    else:
        print(testResults)

# vim: set filetype=python set foldmethod=marker
