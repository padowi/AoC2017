#!/usr/bin/env python3

import sys
import os.path
import datetime

def spin(dancers, num):
    return dancers[-num:] + dancers[:-num]

def partner(dancers, p1, p2):
    tmp = dancers[p1]
    dancers[p1] = dancers[p2]
    dancers[p2] = tmp
    return dancers

def main(data):
    dancers = list("abcdefghijklmnop")
    instructions = data.split(",")
    parsedInstructions = list()
    for instruction in instructions:
        if instruction.startswith('s'):
            parsedInstructions.append( ('s', int(instruction[1:])) )
        elif instruction.startswith('x'):
            posA, posB = instruction[1:].split('/')
            parsedInstructions.append( ('x', int(posA), int(posB)) )
        elif instruction.startswith('p'):
            progA, progB = instruction[1:].split('/')
            parsedInstructions.append( ('p', progA, progB) )

    for i in range(999_999_960, 1_000_000_000):
        # every 60th cycle we begin at the starting point
        # which means that if we start at 999999960 that will be the same thing as starting at 0
        if dancers == list('abcdefghijklmnop'):
            print(i)
        for instruction in parsedInstructions:
            if instruction[0] == 's':
                dancers = spin(dancers, instruction[1])
            elif instruction[0] == 'x':
                dancers = partner(dancers, instruction[1], instruction[2])
            elif instruction[0] == 'p':
                dancers = partner(
                    dancers,
                    dancers.index(instruction[1]),
                    dancers.index(instruction[2])
                )

    return ''.join(dancers)

if __name__ == '__main__':
    # based on calculations, this will take 5 years to complete...
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
        print(main(inputData))
    else:
        print("Input file not found")

# vim: set filetype=python set foldmethod=marker
