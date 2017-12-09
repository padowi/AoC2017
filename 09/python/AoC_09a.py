#!/usr/bin/env python3

import sys
import os.path
import re
from collections import defaultdict

garbagePattern = re.compile(r'<[^>]*>')
ignorePattern = re.compile(r'!.')

def removeIgnored(data):
    return ignorePattern.sub('', data)

def removeGarbage(data):
    return garbagePattern.sub('', data)

def score(tree):
    result = 0
    for k in tree.keys():
        result += k * len(tree[k])
    return result

def main(data):
    tree = defaultdict(list)
    data = removeIgnored(data)
    data = removeGarbage(data)

    depth = 0
    for c in  data:
        if c == '{':
            depth += 1
            tree[depth].append(depth)
        if c == '}':
            depth -= 1
    return tree

if __name__ == '__main__':
    testVectors = {
        # number of valid groups in input, a group is {.*[^!]+?}
        '<>': 0,
        '<random characters>': 0,
        '<<<<>': 0,
        '<{!>}>': 0,
        '<!!>': 0,
        '<!!!>>': 0,
        '<{o"i!a,<{i<a>': 0,
        '{}': 1,
        '{{{}}}': 3,
        '{{},{}}': 3,
        '{{{},{},{{}}}}': 6,
        '{<{},{},{{}}>}': 1,
        '{<a>,<a>,<a>,<a>}': 1,
        '{{<a>},{<a>},{<a>},{<a>}}': 5,
        '{{<!>},{<!>},{<!>},{<a>}}': 2,
    }
    testVectors2 = {
        # "score" is sum of products of depth in tree times nodes at depth
        '{}': 1,
        '{{{}}}': 6,
        '{{},{}}': 5,
        '{{{},{},{{}}}}': 16,
        '{<a>,<a>,<a>,<a>}': 1,
        '{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
        '{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
        '{{<a!>},{<a!>},{<a!>},{<ab>}}': 3,
    }
    
    testResults = [
        sum([ len(e) for e in main(ti).values()]) == tr
        for ti, tr
        in testVectors.items()
    ]
    testResults.extend([
        score(main(ti)) == tr
        for (ti, tr)
        in testVectors2.items()
    ])

    if all(testResults):
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
                inputData = fh.read()
                inputData = inputData.strip()
            print(score(main(inputData)))
        else:
            print("Input file not found")
    else:
        print(testResults)

# vim: set filetype=python set foldmethod=marker
