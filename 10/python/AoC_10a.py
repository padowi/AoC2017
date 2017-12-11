#!/usr/bin/env python3

import sys
import os.path

def deriveIndices(keySpace, curPos, length):
    indices = list()
    for i in range(curPos, curPos + length):
        indices.append(i % len(keySpace))
    return indices

def extract(keySpace, curPos, length):
    output = list()
    for i in deriveIndices(keySpace, curPos, length):
        output.append(keySpace[i])
    return output

def insert(keySpace, curPos, length, subSet):
    indices = deriveIndices(keySpace, curPos, length)
    for (idx, val) in enumerate(subSet):
        keySpace[indices[idx]] = val
    return keySpace

def main(keySpace, inputLengths):
    # do stuff
    curPos = skipSize = 0
    inputLengths = [int(i) for i in inputLengths.split(',')]

    for length in inputLengths:
        subSet = reversed(extract(keySpace, curPos, length))
        keySpace = insert(keySpace, curPos, length, subSet)
        curPos = (curPos + length + skipSize) % len(keySpace)
        skipSize += 1

    endState = list()
    for k in sorted(keySpace.keys()):
        endState.append(keySpace[k])

    return ( endState, endState[0] * endState[1] )

if __name__ == '__main__':
    keySpace = {i: i for i in range(5)}
    inputLengths = "3,4,1,5"
    expectedEndState = [3, 4, 2, 1, 0]
    expectedOutput = 12

    (endState, output) = main(keySpace, inputLengths)
    if expectedEndState == endState and expectedOutput == output:
        del keySpace
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
                keySpace = {i: i for i in range(256)}
                inputData = fh.read()
            output = main(keySpace, inputData)
            endState = output[0]
            answer = output[1]
            print(answer)
        else:
            print("Input file not found")
    else:
        print("Tests failed!")

# vim: set filetype=python set foldmethod=marker
