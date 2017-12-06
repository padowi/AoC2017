#!/usr/bin/env python3

import os.path
import sys

def first(data):
    idx = 0
    nxt = (idx + int(len(data)/2)) % len(data)
    
    result = 0

    exitLoop = False
    wrapped = False

    while True:
        if idx == len(data) - 1:
            if data[idx] == data[nxt]:
                result += int(data[idx])
            break

        if data[idx] == data[nxt]:
            result += int(data[idx])

        idx = (idx + 1) % len(data)
        nxt = (idx + int(len(data)/2)) % len(data)

    return result

def improved(n):
    result = 0
    for (idx, num) in enumerate(n):
        if num == n[(idx+int(len(n)/2))%len(n)]:
            result += int(num)
    return result

def reddit(n):
    return (2 * sum(int(x) for x, y in zip(n, n[len(n) // 2:]) if x == y))

def main(n):
    return improved(n)

if __name__ == '__main__':
    testVectors = {
        '1212': 6,
        '1221': 0,
        '123425': 4,
        '123123': 12,
        '12131415': 4,
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
