#!/usr/bin/env python3

import sys
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
