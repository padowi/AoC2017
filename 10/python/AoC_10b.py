#!/usr/bin/env python3

import sys
import os.path
import functools

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

def xor(a, b):
    return a ^ b

def main(keySpace, inputLengths):
    curPos = skipSize = 0
    inputLengths = [ord(c) for c in inputLengths]
    adds = [17, 31, 73, 47, 23]
    inputLengths.extend(adds)

    for _ in range(64):
        for length in inputLengths:
            subSet = reversed(extract(keySpace, curPos, length))
            keySpace = insert(keySpace, curPos, length, subSet)
            curPos = (curPos + length + skipSize) % len(keySpace)
            skipSize += 1

    sparseHash = keySpace
    
    blocks = list()
    tmpList = list()

    for k in sorted(keySpace.keys()):
        if k % 16 == 0 and len(tmpList) > 0:
            blocks.append(tmpList)
            tmpList = list()
        tmpList.append(keySpace[k])
    blocks.append(tmpList)
    
    hashes = list()
    for block in blocks:
        hashes.append(functools.reduce(xor, block))

    result = ''
    for h in hashes:
        tmp = hex(h).lstrip('0x')
        if len(tmp) == 1:
            tmp = '0' + tmp
        result += tmp
    return result

if __name__ == '__main__':
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
            inputData = inputData.strip()
        output = main(keySpace, inputData)
        print(output)
    else:
        print("Input file not found")

# vim: set filetype=python set foldmethod=marker
