#!/usr/bin/env python3

import sys
import os.path
from itertools import cycle

"""
Perhaps we should attack this from a mathematical direction...
in sector 0 we have a scanner. It starts at position 0 in sector 0.
It has a depth of 2.
So at picosecond 0 we move into sector 0 (position 0),
just as the scanner moves on to position 1
With a depth of 2, the scanner has hit a boundary and turned around
At picosecond 1 it is moving back into position 0
If it moves into the same position we are at, we are detected, so we have to
get our butt out of there before that time, but that's not a problem as we
always move one step forward for each picosecond
But this means also that in order to not get caught at sector 0
we can only begin our journey on even picoseconds
"""

def firewall(mapping):
# {{{
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
# }}}

def cycleLength(depth):
    return (depth * 2) - 2
def detected(t, fw):
    pass

def create_cycle(depth):
    tmp = list(range(depth))
    tmp.extend(reversed(tmp[1:-1]))
    return cycle(tmp)

def setup(mapping):
    pass

def main(mapping):
    # according to problem, 10 is the smallest delay allowed
    delay = 0

    while True:
        print("Trying with delay: {}".format(delay))
        detected = list()
        fw = firewall(mapping)
        curPos = -1
        dest = max(mapping.keys()) + 1
        layers = sorted(fw.keys())

        # introduce the delay
        # {{{
        for _ in range(delay):
            for k in layers:
                if fw[k]:
                    fw[k].__next__()
        # }}}

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

        if len(detected) == 0:
            break
        else:
            delay += 1

    return delay
    


if __name__ == '__main__':
# {{{
    testVectors = (
            ({0:3, 1:2, 4:4, 6:4}, 10),
    )
    
    # 17842 is too high
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
# }}}

# vim: set filetype=python set foldmethod=marker
