#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Dijkstra's shortest path algorithm.
# Compute the shortest path between the source vertex and all the other
# reachable vertices.

import heapq
from collections import defaultdict

class Vertex():
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.outgoing = set()
        self.distance = 0

def build_graph(input_file):
    graph = {}

    for line in input_file:
        items = line.split()
        head = int(items[0])
        graph[head] = Vertex(head)
        for path in items[1:]:
            tail, length = (int(x) for x in path.split(','))
            graph[head].outgoing.add((length, tail))

    return graph

def find_shortest_paths(graph, source):
    assert type(source) == int
    frontier = list(graph[source].outgoing)
    heapq.heapify(frontier)
    visited = set([source])

    while frontier:
        distance, head = heapq.heappop(frontier)
        if head in visited:
            continue
        visited.add(head)
        if head not in graph.iterkeys():
            continue
        graph[head].distance = distance

        for new_distance, tail in graph[head].outgoing:
            edge = (new_distance + distance, tail)
            heapq.heappush(frontier, edge)


if __name__ == '__main__':
    with open('data/dijkstraData.txt') as fin:
        graph = build_graph(fin)

    source = 1
    find_shortest_paths(graph, source)

    paths = []
    for destination in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
        shortest_path = graph[destination].distance
        if shortest_path == 0:
            shortest_path = 1000000
        paths.append(shortest_path)
    print ','.join([str(path) for path in paths])
