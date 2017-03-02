#!/usr/bin/env python
import itertools
import operator
import sys
import ast
import heapq

def parsePairs():
    for line in sys.stdin:
        yield tuple(line.strip('\n').split('\t'))

def reducer(k):
    for key, pairs in itertools.groupby(parsePairs(),
                                       operator.itemgetter(0)):
        result = []
        for p in pairs:
            topk = ast.literal_eval(p[1])
            result = heapq.nlargest(k, result + topk, lambda line: int(line.strip('\n').split('\t')[1]))
        for i in result:
            print ':'.join(i.strip('\n').split('\t'))

if __name__=='__main__':
    reducer(3)
