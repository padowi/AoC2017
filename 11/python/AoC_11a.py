#!/usr/bin/env python3

import sys
import os.path

class HexNode(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = {
            'nw': (x-0.5, y+0.5),
            'n': (x, y+1),
            'ne': (x+0.5, y+0.5),
            'sw': (x-0.5, y-0.5),
            's': (x, y-1),
            'se': (x+0.5, y-0.5),
        }
    def get(self, d):
        return self.neighbors[d]


move = {
    'n': north,
    's': south,
    'nw': nw,
    'ne': ne,
    'sw': sw,
    'se': se,
}

def nw(coord):
    x, y = coord
    return (x-0.5, y+0.5)
def n(coord):
    x, y = coord
    return (x, y+1)
def ne(coord):
    x, y = coord
    return (x+0.5, y+0.5)
def sw(coord):
    x, y = coord
    return (x-0.5, y-0.5)
def s(coord):
    x, y = coord
    return (x, y-1)
def se(coord):
    x, y = coord
    return (x+0.5, y-0.5)

def main(data):
    steps = data.split(',')
    origin = (0.0, 0.0)
    coords = list()
    coords.append(origin)

    for s in steps:
        coords.append(move[s](coords[-1]))

    # we need a BFS here...
    print(coords)

    location = coords[-1]


if __name__ == '__main__':
    testVectors = {
        'ne,ne,ne': 3,
        'ne,ne,sw,sw': 0,
        'ne,ne,s,s': 2,
        'se,sw,se,sw,sw': 3,
    }
    
    testResults = [ main(ti) == eo for (ti, eo) in testVectors.items() ]
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
            print(main(inputData))
        else:
            print("Input file not found")
    else:
        print(testResults)

# vim: set filetype=python set foldmethod=marker
