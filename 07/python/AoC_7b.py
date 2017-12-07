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

    def setWeight(self, w):
        self.weight = w

    def setParent(self, p):
        self.parent = p

    def hasParent(self):
        return self.parent is not None

    def getParent(self):
        return self.parent

    def addChild(self, c):
        self.children.append(c)

    def getName(self):
        return self.name

    def getOwnWeight(self):
        return self.weight

    def getWeight(self):
        tmpWeight = 0
        if self.hasChildren():
            for c in self.getChildren():
                tmpWeight += c.getWeight()
        return self.getOwnWeight() + tmpWeight

    def hasChildren(self):
        return len(self.children) > 0

    def getChildren(self):
        return self.children

    def getChildByWeight(self, weight):
        child = None
        if self.hasChildren():
            for c in self.getChildren():
                if weight == c.getWeight():
                    child = c
        return child
    def __str__(self):
        return self.name
    def __repr__(self):
        return "<Node({}, {})[{}]>".format(
            self.getName(),
            self.getOwnWeight(),
            self.getWeight()
        )

    def balanced(self):
        """
        a node is balanced if all its children report back the same weight
        """
        if not self.hasChildren():
            return True
        childWeights = set()
        for c in self.getChildren():
            childWeights.add(c.getWeight())
        return len(childWeights) == 1
# }}}    

def main(data):
    nodes = dict()
    lines = list()
    for line in data:
        elems = line.split()
        elems = [e.strip('(),') for e in elems]
        if len(elems) > 2:
            lines.append(elems)
        name, weight = elems[0], int(elems[1])
        nodes[name] = Node(name, weight)

    for elems in lines:
        parentName = elems[0]
        parent = nodes[parentName]
        childNames = elems[3:]

        for childName in childNames:
            nodes[childName].setParent( nodes[parentName] )
            parent.addChild( nodes[childName] )

    unbalancedNodes = [n for n in nodes.values() if not n.balanced()]
    # an unbalanced node will for sure have unbalanced children, but we're interested in the parent
    for node in unbalancedNodes:
        if node.hasParent():
            if not node.getParent() in unbalancedNodes:
                break

    # this node has children who's weights are not balanced
    print(node.__repr__())
    children = node.getChildren()

    weightList = [c.getWeight() for c in children]
    weightSet = set(weightList)

    for w in weightSet:
        if weightList.count(w) == 1:
            offender = w
    for w in weightSet:
        if weightList.count(w) > 1:
            norm = w
    offendingNode = node.getChildByWeight(offender)

    nodeOwnWeight = offendingNode.getOwnWeight()
    nodeWeight = offendingNode.getWeight()
    childWeights = nodeWeight - nodeOwnWeight

    targetWeight = norm

    if norm > offender:
        newWeight = nodeOwnWeight + (targetWeight - nodeOwnWeight)
    else:
        newWeight =  targetWeight - childWeights

    return newWeight

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

    if main(testInput) == 60:
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
