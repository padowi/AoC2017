#!/usr/bin/env python3

import sys
import os.path

def spin(dancers, num):
    return dancers[-num:] + dancers[:-num]

def partner(dancers, p1, p2):
    tmp = dancers[p1]
    dancers[p1] = dancers[p2]
    dancers[p2] = tmp
    return dancers

def main(data):
    dancers = list("abcdefghijklmnop")
    for instruction in data.split(","):
        if instruction.startswith("s"):
            dancers = spin(dancers, int(instruction[1:]))
        elif instruction.startswith("x"):
            posA, posB = instruction[1:].split('/')
            posA = int(posA)
            posB = int(posB)
            dancers = partner(dancers, posA, posB)
        elif instruction.startswith("p"):
            progA, progB = instruction[1:].split('/')
            posA = dancers.index(progA)
            posB = dancers.index(progB)
            dancers = partner(dancers, posA, posB)
    return ''.join(dancers)

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
            inputData = fh.read()
        print(main(inputData))
    else:
        print("Input file not found")

# vim: set filetype=python set foldmethod=marker
