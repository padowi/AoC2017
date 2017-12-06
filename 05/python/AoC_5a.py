#!/usr/bin/env python3

import os.path

class Node(object):
    def __init__(self, offset):
        self.offset = offset

    def increment(self):
        self.offset += 1

    def get_offset(self):
        return self.offset

def main(data):
    nodes = list()
    for e in data:
        node = Node(e)
        nodes.append(node)

    pos = 0
    node = nodes[pos]
    counter = 0

    while True:
        counter += 1
        offset = node.get_offset()
        node.increment()
        pos = pos + offset

        if 0 <= pos < len(nodes):
            node = nodes[pos]
        else:
            break

    return counter

if __name__ == '__main__':
    testVectors = [
        ([0, 3, 0, 1, -3], 5)
    ]

    testResults = [ main(t[0]) == t[1] for t in testVectors ]
    if all(testResults):
        print("All tests passed!")
        if os.path.isfile("../input"):
            with open('../input', 'r') as fh:
                inputData = fh.readlines()
                inputData = [int(e.strip()) for e in inputData]
            print(main(inputData))
        else:
            print("Input file not found")
    else:
        print(testResults)
