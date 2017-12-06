#!/usr/bin/env python3

import os.path

def rowVal(line):
    line = line.strip()
    values = [int(v) for v in line.split() if len(v) > 0 ]
    values.sort()
    values.reverse()
    while values:
        exponent = values.pop(0)
        for divisor in values:
            if exponent % divisor == 0:
                return exponent // divisor

def checksum(data):
    return sum([rowVal(r) for r in data])

if __name__ == '__main__':
    testVectors = {
        "5   9   2   8": 4,
        "9   4   7   3": 3,
        "3   8   6   5": 2
    }
    
    testResults = [rowVal(ti) == testVectors[ti] for ti in testVectors.keys()]
    testResults.append( checksum(list(testVectors.keys())) == 9 )

    if all(testResults):
        print("All tests passed!")
        if os.path.isfile("../input"):
            with open('../input', 'r') as fh:
                print(checksum(fh.readlines()))
        else:
            print("Input file not found")
    else:
        print(testResults)
