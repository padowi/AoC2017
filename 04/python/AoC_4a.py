#!/usr/bin/env python3

import os.path

def first(lines):
    valid = 0
    for line in lines:
        line = line.strip()
        words = line.split()
        if len(words) == len(set(words)):
            valid += 1
    return valid


def main(data):
    return first(data)

if __name__ == '__main__':
    testVector = [
        'aa bb cc dd ee',
        'aa bb cc dd aa',
        'aa bb cc dd aaa',
    ]
    
    testResult = main(testVector)
    if testResult == 2:
        print("All tests passed!")
        if os.path.isfile("../input"):
            with open('../input', 'r') as fh:
                inputData = fh.readlines()
            print(main(inputData))
        else:
            print("Input file not found")
    else:
        print(testResult)
