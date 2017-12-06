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

def improved(target):
    coords = list()
    iteration = 0
    coords.append( (0, 0) )
    directions = ['right', 'up', 'left', 'down']

    while len(coords) < target:
        for d in directions:
            if d in ['right', 'up']:
                delta = (iteration * 2) + 1
            else:
                delta = (iteration * 2) + 2
            for _ in range(delta):
                tmpCoord = coords[-1]
                coords.append( deriveMove( tmpCoord, d ) )
        iteration += 1

    t = coords[target - 1]
    print("target: {}, coord: {}, moves: {}".format(target, t, abs(t[0]) + abs(t[1])))
    return abs(t[0]) + abs(t[1])

def naive(targetNum):
# {{{
    nodes = list()

    currentNum = 1
    originCoord = currentCoord = (0, 0)
    nodes.append(currentCoord)
    nextMove = 'right'

    while not currentNum == targetNum:
        currentNum += 1
        if currentNum % 1000 == 0:
            print(currentNum)
            print("{} nums left".format(targetNum - currentNum))
        tmpCoord = deriveMove(currentCoord, nextMove)
        nodes.append(tmpCoord)
        currentCoord = tmpCoord

        # now we need to derive the direction of nextMove
        if nextMove == 'right':
            # we should either continue right, or up
            # we change direction when the up-move-coord does not generate a match in nodes
            if not deriveMove(currentCoord, 'up') in nodes:
                nextMove = 'up'
            #else: continue right 
        elif nextMove == 'up':
            # we should either continue up, or go left
            # we change direction when the left-move-coord does not generate a match in nodes
            if not deriveMove(currentCoord, 'left') in nodes:
                nextMove = 'left'
            #else: continue up
        elif nextMove == 'left':
            # we should either continue left, or go down
            # we change direction when the down-move-coord does not generate a match in nodes
            if not deriveMove(currentCoord, 'down') in nodes:
                nextMove = 'down'
            #else: continue left
        else: #nextMove == 'down'
            # we should either continue down, or go right
            # we change direction when the right-move-coord does not generate a match in nodes
            if not deriveMove(currentCoord, 'right') in nodes:
                nextMove = 'right'
            #else: continue down
    # print("num: {}, coord: {}".format(currentNum, currentCoord))
    return abs(currentCoord[0] + currentCoord[1])
# }}}

def main(targetNum):
    return improved(targetNum)


if __name__ == '__main__':
    testVectors = {
        1: 0,
        2: 1,
        3: 2,
        4: 1,
        5: 2,
        6: 1,
        7: 2,
        8: 1,
        9: 2,
        10: 3,
        12: 3,
        23: 2,
        1024: 31
    }

    testResults = [ main(ti) == testVectors[ti] for ti in testVectors.keys() ]
    print(testResults)
    print(main(265149))
