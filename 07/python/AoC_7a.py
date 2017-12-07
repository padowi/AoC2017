#!/usr/bin/env python3

import sys
import os.path

class Node(object):
# {{{
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None

    def size(self):
        return len(self.children)

    def setWeight(self, w):
        self.weight = w

    def setParent(self, p):
        self.parent = p

    def hasParent(self):
        return self.parent is not None

    def addChild(self, c):
        self.children.append(c)

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getChildren(self):
        return self.children

    def __str__(self):
        return self.name
    def __repr__(self):
        return "<Node({})[{}]>".format(
            self.name,
            ', '.join(self.children)
        )
# }}}    

def main(data):
    nodes = dict()
    lines = list()
    for line in data:
        elems = line.split()
        elems = [e.strip('(),') for e in elems]
        if len(elems) > 2:
            lines.append(elems)
        name, weight = elems[0], elems[1]
        nodes[name] = Node(name, weight)

    for elems in lines:
        parentName = elems[0]
        parent = nodes[parentName]
        childNames = elems[3:]

        for childName in childNames:
            nodes[childName].setParent( nodes[parentName] )
            parent.addChild( nodes[childName] )

    for node in nodes.keys():
        if not nodes[node].hasParent():
            return node

if __name__ == '__main__':
    testInput = [
        "pbga (66)",
        "xhth (57)",
        "ebii (61)",
        "havc (66)",
        "ktlj (57)",
        "fwft (72) -> ktlj, cntj, xhth",
        "qoyq (66)",
        "padx (45) -> pbga, havc, qoyq",
        "tknk (41) -> ugml, padx, fwft",
        "jptl (61)",
        "ugml (68) -> gyxo, ebii, jptl",
        "gyxo (61)",
        "cntj (57)",
    ]

    if main(testInput) == "tknk":
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

# vim: set ft=python set foldmethod=marker
