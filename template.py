#!/usr/bin/env python3

import os.path

def main(data):
    pass

if __name__ == '__main__':
    testVectors = {
        '': 0,
    }
    
    testResults = [ main(ti) == testVectors[ti] for ti in testVectors.keys() ]
    if all(testResults):
        print("All tests passed!")
        if os.path.isfile("../input"):
            with open('../input', 'r') as fh:
                inputData = fh.read()
                inputData = inputData.strip()
            print(main(inputData))
        else:
            print("Input file not found")
    else:
        print(testResults)
