#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

class Vertex():
    def __init__(self, key):
        self.key = key
        self.parent = self

def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)

    if root1 < root2:
        root1.parent = root2
    else:
        root2.parent = root1
    
def find(vertex):
    if vertex.parent != vertex:
        vertex.parent = find(vertex.parent)

    return vertex


if __name__ == '__main__':
    seen = {}
    with open(sys.argv[1]) as fin:
        for line in fin:
            items = [int(x) for x in line.split()]
            items[3] -= items[3] % 10

            key1 = items[0], items[1]
            if key1 not in seen:
                 vertex1 = Vertex(key1)
            seen[key1] = vertex1

            key2 = items[2], items[3]
            if key2 not in seen:
                 vertex2 = Vertex(key2)
            seen[key2] = vertex2

            union(vertex1, vertex2)
