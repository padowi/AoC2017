#!/usr/bin/env python3

import os.path

def rowVal(line):
    line = line.strip()
    values = [int(v) for v in line.split() if len(v) > 0]
    return max(values) - min(values)

def checksum(data):
    return sum([rowVal(r) for r in data])

if __name__ == '__main__':
    testVectors = {
        "5 1 9 5": 8,
        "7 5 3": 4,
        "2 4 6 8": 6
    }
    
    testResults = [rowVal(ti) == testVectors[ti] for ti in testVectors.keys()]
    testResults.append( checksum(list(testVectors.keys())) == 18 )

    if all(testResults):
        print("All tests passed!")
        if os.path.isfile("../input"):
            with open('../input', 'r') as fh:
                print(checksum(fh.readlines()))
        else:
            print("Input file not found")
    else:
        print(testResults)
