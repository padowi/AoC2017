#!/usr/bin/env python3

import sys
import os.path

def bankWithMostBlocks(banks):
    return sorted(list(banks.items()), key=lambda e: e[1], reverse=True)[0][0]

def main(data):
    dataLength = len(data)
    configurations = set()
    configuration = tuple(list(data.values()))

    while configuration not in configurations:
        configurations.add(configuration)
        bankIdx = bankWithMostBlocks(data)
        blocksToRedistribute = data[bankIdx]
        data[bankIdx] = 0
        while blocksToRedistribute > 0:
            bankIdx = (bankIdx + 1) % dataLength
            data[bankIdx] += 1
            blocksToRedistribute -= 1
        configuration = tuple(list(data.values()))

    counter = 0
    configTarget = configuration

    while True:
        if configuration == configTarget and counter > 0:
            break
        counter += 1
        bankIdx = bankWithMostBlocks(data)
        blocksToRedistribute = data[bankIdx]
        data[bankIdx] = 0
        while blocksToRedistribute > 0:
            bankIdx = (bankIdx + 1) % dataLength
            data[bankIdx] += 1
            blocksToRedistribute -= 1
        configuration = tuple(list(data.values()))

    return counter

if __name__ == '__main__':
    testVectors = [
        ({0: 0, 1: 2, 2: 7, 3: 0}, 4),
    ]

    testResults = [ main(ti[0]) == ti[1] for ti in testVectors ]
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
                inputData = { i: int(e) for i, e in enumerate( inputData.split() ) }
            print(main(inputData))
        else:
            print("Input file not found")
    else:
        print(testResults)
        print(main({0: 0, 1: 2, 2: 7, 3: 0}))
