#!/usr/bin/env python3

import os.path

def first(lines):
    valid = 0
    for line in lines:
        line = line.strip()
        words = line.split()

        tmpList = list()
        tmpSet = set()
        for w in words:
            w = ''.join(sorted(w))
            tmpList.append(w)
            tmpSet.add(w)
        if len(tmpList) == len(tmpSet):
            valid += 1
    return valid


def main(data):
    return first(data)

if __name__ == '__main__':
    testVector = [
        'abcde fghij',
        'abcde xyz ecdab',
        'a ab abc abd abf abj',
        'iiii oiii ooii oooi oooo',
        'oiii ioii iioi iiio',
    ]
    
    testResult = main(testVector)
    if testResult == 3:
        print("All tests passed!")
        if os.path.isfile("../input"):
            with open('../input', 'r') as fh:
                inputData = fh.readlines()
            print(main(inputData))
        else:
            print("Input file not found")
    else:
        print(testResult)
