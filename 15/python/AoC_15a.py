#!/usr/bin/env python3

import sys
import os.path

def generatorA(num):
    factor = 16807
    divi = 2147483647
    return (num * factor) % divi

def generatorB(num):
    factor = 48271
    divi = 2147483647
    return (num * factor) % divi

def judge(a, b):
    b16a = bin(a)[-16:]
    b16b = bin(b)[-16:]
    return (b16a, b16b)


def main(data):
    a = data['a']
    b = data['b']
    matches = 0
    for i in range(40_000_000):
        if i % 100_000 == 0:
            print(i)
        a = generatorA(a)
        b = generatorB(b)
        b16a, b16b = judge(a, b)
        if b16a == b16b:
            matches += 1
    return matches

if __name__ == '__main__':
    testVector = {
        'in': {'a': 65, 'b': 8921},
        'out': 588
    }
    
    if main(testVector['in']) == testVector['out']:
        print("All tests passed!")
        inputData = {'a': 277, 'b': 349}
        print("Answer: {}".format(main(inputData)))

# vim: set filetype=python set foldmethod=marker
