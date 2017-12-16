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
    for i in range(1_000_000_000):
        if i % 10_000 == 0:
            print("Iteration {} * 10_000: {} (start)".format(i, datetime.datetime.now()))
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
        if i % 10_000 == 0:
            print("Iteration {} * 10_000: {} (end)".format(i, datetime.datetime.now()))
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
