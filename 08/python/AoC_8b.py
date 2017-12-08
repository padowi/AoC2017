#!/usr/bin/env python3

import sys
import os.path
from collections import defaultdict

def eq(a, b):
    return a == b
def lt(a, b):
    return a < b
def lte(a, b):
    return a <= b
def gt(a, b):
    return a > b
def gte(a, b):
    return a >= b
def neq(a, b):
    return a != b

def main(data):
    registers = defaultdict(lambda: 0)
    highest = 0
    comps = {
        '==': eq,
        '<': lt,
        '<=': lte,
        '>': gt,
        '>=': gte,
        '!=': neq
    }
    for instruction in data:
        (reg, op, val, _, otherReg, comp, otherVal) = instruction.split(' ')
        val = int(val)
        otherVal = int(otherVal)
        if comps[comp](registers[otherReg], otherVal):
            if op == 'dec':
                registers[reg] -= val
            else:
                registers[reg] += val
            highest = max(highest, registers[reg])
    return highest

if __name__ == '__main__':
    testVectors = [
        "b inc 5 if a > 1",
        "a inc 1 if b < 5",
        "c dec -10 if a >= 1",
        "c inc -20 if c == 10",
    ]
    
    if main(testVectors) == 10:
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
