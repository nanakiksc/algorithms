#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Tarjan's Union-Find algorithm.
# Find all the connected components (cc) in an undirected graph
# by means of path compression to the parent vertex of each cc.
# Parent is arbitrarily chosen among all cc vertices.

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
    elif root1 > root2:
        root2.parent = root1
    
def find(vertex):
    if vertex.parent != vertex:
        vertex.parent = find(vertex.parent)

    return vertex

def main(input_file):
    graph = {}
    for line in input_file:
        key1, key2 = [int(x) for x in line.split()]

        if key1 not in graph:
             graph[key1] = Vertex(key1)

        if key2 not in graph:
             graph[key2] = Vertex(key2)

        union(graph[key1], graph[key2])

    return graph


if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        graph = main(fin)
