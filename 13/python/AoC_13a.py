#!/usr/bin/env python3

import sys
import os.path
from itertools import cycle

def firewall(mapping):
    fw = dict()
    maxLayer = max(mapping.keys()) + 1

    for layer in range(maxLayer):
        depth = mapping.get(layer, None)
        if depth:
            elements = list(range(depth))
            sublist = reversed(elements[1:-1])
            elements.extend(sublist)
            fw[layer] = cycle(elements)
        else:
            fw[layer] = None
    return fw

def main(mapping):
    fw = firewall(mapping)
    curPos = -1
    dest = max(mapping.keys()) + 1
    layers = sorted(fw.keys())
    detected = list()

    while not curPos == dest:
        # move all scanners
        scanPos = dict()
        for k in layers:
            if fw[k]:
                scanPos[k] = fw[k].__next__()
            else:
                fw[k] = None

        # advance position
        curPos += 1
        # avoid edge case where there isn't a scanner in our area of operations

        obj = scanPos.get(curPos, None)
        if obj == None:
            continue

        # check if we got detected
        if obj == 0:
            detected.append(curPos)
    severity = 0
    for d in detected:
        severity += d * mapping[d]
    return severity
    


if __name__ == '__main__':
    testVectors = (
            ({0:3, 1:2, 4:4, 6:4}, 24),
    )
    
    testResults = [ main(ti) == eo for (ti, eo) in testVectors ]
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
                inputData = fh.readlines()
                mapping = dict()
                for line in inputData:
                    k, v = line.split(': ')
                    mapping[int(k)] = int(v)
            print(main(mapping))
        else:
            print("Input file not found")
    else:
        print(testResults)

# vim: set filetype=python set foldmethod=marker
