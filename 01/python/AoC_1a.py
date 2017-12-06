#!/usr/bin/env python3

import os.path
import sys

def first(data):
    idx = 0
    nxt = (idx + 1) % len(data)
    
    result = 0

    exitLoop = False
    wrapped = False

    while True:
        if nxt < idx:
            if data[idx] == data[nxt]:
                result += int(data[idx])
            break

        if data[idx] == data[nxt]:
            result += int(data[idx])

        idx = nxt
        nxt = (idx + 1) % len(data)

    return result

def improved(n):
    result = 0
    for (idx, num) in enumerate(n):
        if num == n[(idx+1)%len(n)]:
            result += int(num)
    return result

def reddit(n):
    return sum(int(x) for x, y in zip(n[-1] + n, n) if x == y)

def main(n):
    return improved(n)

if __name__ == '__main__':
    testVectors = {
        '1122': 3,
        '1111': 4,
        '1234': 0,
        '91212129': 9
    }
    
    testResults = [ main(ti) == testVectors[ti] for ti in testVectors.keys() ]
    if all(testResults):
        print("All tests passed!")
        if os.path.isfile("../input"):
            with open('../input', 'r') as fh:
                inputData = fh.read()
                inputData = inputData.strip()
            print(main(inputData))
        else:
            print("Input file not found")
    else:
        print(testResults)
