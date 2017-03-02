#!/usr/bin/env python
import sys
import heapq

def mapper(k):
    topk = heapq.nlargest(k, sys.stdin,
                          lambda line: int(line.strip('\n').split('\t')[1]))
    print '0\t%s' % topk

if __name__=='__main__':
    mapper(3)
