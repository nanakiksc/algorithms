#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import copy

def choose_min_cut(graph):
    # Count the number of crossing vertices in the cut.
    cut_graph = random_contraction(graph)
    edges = []
    for vertex in cut_graph:
        edges.append(cut_graph[vertex])
    assert len(edges) == 2
    assert len(edges[0]) == len(edges[1])

    return len(edges[0])

def random_contraction(graph):
    # Return a contracted version of the grapf with only 2 meta-vertices.
    vertices = graph.keys()
    while len(vertices) > 2:

        # Randomly choose 2 connected vertices.
        vertex1 = random.choice(vertices)
        edges1 = graph[vertex1]
        vertex2 = random.choice(edges1)
        edges2 = graph[vertex2]

        # Use one of the vertices as meta-vertex.
        graph[vertex1] = edges1 + edges2
        
        # Remove "self-loops".
        while vertex1 in graph[vertex1]:
            graph[vertex1].remove(vertex1)
        while vertex2 in graph[vertex1]:
            graph[vertex1].remove(vertex2)

        # Remove the other vertex and update references to it.
        del graph[vertex2]
        for vertex in graph:
            while vertex2 in graph[vertex]:
                graph[vertex].remove(vertex2)
                graph[vertex].append(vertex1)

        vertices = graph.keys()

    return graph

if __name__ == '__main__':
    graph = {}
    # Read input file and build graph.
    with open('kargerMinCut.txt') as fin:
        for row in fin:
            edges = [int(vertex) for vertex in row.split()]
            graph[edges.pop(0)] = edges

    cuts = []
    for i in xrange(len(graph) - 1): # Min # iters to guarantee the solution.
        working_graph = {}
        # Generate a new instance of the graph in each iteration
        # to avoid aliasing.
        for vertex in graph:
            if vertex not in working_graph:
                working_graph[vertex] = []
            for edge in graph[vertex]:
                working_graph[vertex].append(edge)

        # Keep track of the number of crossing edges after each cut.
        cuts.append(choose_min_cut(working_graph))

    print min(cuts)
