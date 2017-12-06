#!/usr/bin/env python3

import os.path

# 445 is too high

def deriveMove(c, direction):
    moves = {
        'right': (c[0]+1, c[1]),
        'left': (c[0]-1, c[1]),
        'up': (c[0], c[1]-1),
        'down': (c[0], c[1]+1)
    }
    return moves[direction]

def neighbours(c):
    # technically, we are also returning ourselves, not just our neighbours,
    # but it doesn't matter
    return [ ( x, y ) for x in range( c[0] - 1, c[0] + 2) for y in range( c[1] - 1, c[1] + 2 ) ]

def deriveCoordValue(coords, c):
    num = 0
    for n in neighbours(c):
        num += coords.get(n, 0)
    return num

def improved(target):
    coords = list()
    coordNumMap = dict()
    iteration = 0
    coords.append( (0, 0) )
    nodeValue = 1
    coordNumMap[(0,0)] = nodeValue
    directions = ['right', 'up', 'left', 'down']

    while nodeValue < target:
        for d in directions:
            if d in ['right', 'up']:
                delta = (iteration * 2) + 1
            else:
                delta = (iteration * 2) + 2
            for _ in range(delta):
                tmpCoord = coords[-1]
                coords.append( deriveMove( tmpCoord, d ) )
                nodeValue = deriveCoordValue(coordNumMap, tmpCoord)
                coordNumMap[tmpCoord] = nodeValue
                if nodeValue > target:
                    return nodeValue
        iteration += 1

    return nodeValue

def main(targetNum):
    return improved(targetNum)


if __name__ == '__main__':
    testVectors = {
    }

    testResults = [ main(ti) == testVectors[ti] for ti in testVectors.keys() ]
    # not 1009457
    print(main(265149))
