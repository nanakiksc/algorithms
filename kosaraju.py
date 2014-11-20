#!/usr/bin/env python
#-*- coding:utf-8 -*-

# First, compute the "magical ordering" of the vertices by traversing the graph
# via forward_DFS, then run DFS_loop in order using forward_DFS.

import sys
from collections import defaultdict

class Vertex():
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.visited = False
        self.incoming = set()
        self.outgoing = set()

    def __repr__(self):
        return str(self.vertex_id)

def format_vertices(line):
    """ Format lines from (head_scaff, head_coord, tail_scaff, tail_coord)
    to (head_scaff, head_coord), (tail_scaff, floor10(tail_coord)). """

    items = [int(item) for item in line.split()]
    items[-1] -= items[-1] % 10 # Round down to tens.
    head, tail = tuple(items[:2]), tuple(items[2:])

    return head, tail

def build_graph(fin):
    """ Dict with one entry per vertex object. Each object contains all
    incoming and outgoing edges to other vertex objects. """

    graph = {}
    for line in fin:
        #head, tail = [int(vertex) for vertex in line.split()]
        # No need to format if vertices are already head-tail pairs.
        head, tail = format_vertices(line)

        if not head in graph:
            graph[head] = Vertex(head)
        if not tail in graph:
            graph[tail] = Vertex(tail)

        graph[head].outgoing.add(graph[tail])
        graph[tail].incoming.add(graph[head])

    return graph

def sort_vertices(graph):
    """ Topologically sort the graph.
    Compute finishing times for every vertex using DFS on the reversed
    order graph. Return a dict = { finish_time: Vertex }. """

    stack = []
    finish_time = 0
    order = {}

    for _, vertex in graph.iteritems():
        if vertex.visited:
            continue

        assert not stack
        vertex.visited = True
        stack.append(vertex)

        while stack:
            vertex = stack[-1]

            if all(head.visited for head in vertex.incoming):
                order[finish_time] = stack.pop()
                finish_time += 1
                continue

            for head in vertex.incoming:
                if not head.visited:
                    head.visited = True
                    stack.append(head)
                    break

    assert len(order) == len(graph)
    return order

def compute_SCC(graph, order):
    """ Do a DFS on the graph in descending order and discover all SCCs
    one by one. Return a dict = { SCC: set(vertices) }. """

    stack = []
    SCC_num = 0
    SCCs = defaultdict(set)

    # Iterate over the graph in descending order of sort_vertices().
    vertices = (order[ft] for ft in xrange(len(order)-1, -1, -1))
    for vertex in vertices:
        if vertex.visited:
            continue

        assert not stack
        vertex.visited = True
        leader = vertex
        stack.append(vertex)

        while stack:
            vertex = stack[-1]
            SCCs[SCC_num].add(vertex)

            if all(tail.visited for tail in vertex.outgoing):
                SCCs[SCC_num].add(stack.pop())
                if vertex == leader: 
                    SCC_num += 1
                continue

            for tail in vertex.outgoing:
                if not tail.visited:
                    tail.visited = True
                    stack.append(tail)
                    break

    assert_sum = 0
    for _, SCC in SCCs.iteritems():
        assert_sum += len(SCC)
    assert assert_sum == len(graph)
    return SCCs


if __name__ == '__main__':
    print 'Read file and build graph...'
    with open(sys.argv[1]) as fin:
        graph = build_graph(fin)

    # First pass.
    print 'First pass...'
    order = sort_vertices(graph)

    # Reinitialize visited statuses.
    print 'Reinitializing graph...'
    for _, vertex in graph.iteritems():
        vertex.visited = False

    # Second pass.
    print 'Second pass...'
    SCCs = compute_SCC(graph, order)
    
    print 'Summarize SCCs...'
    SCC_sizes = []
    for _, SCC in SCCs.iteritems():
        SCC_sizes.append(len(SCC))
    #print len([i for _, i in SCCs.iteritems() if len(i) == 1])
    print sorted(SCC_sizes)[len(SCC_sizes)-10:]
