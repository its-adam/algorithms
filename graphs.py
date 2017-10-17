#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  graphs.py
#


"""library of graph algorithms"""

from random import randrange
from random import sample


# karger min cut


def choose_edge(graph):
    vertex1 = sample(graph.keys(), 1)[0]
    index2 = randrange(len(graph[vertex1]))
    vertex2 = graph[vertex1][index2]
    edge = (vertex1, vertex2)
    return edge


def contract_edge(graph, edge):
    debug = False
    # contracting an edge means merging the vertices
    vertex1 = edge[0]
    vertex2 = edge[1]

    # new vertex name
    super_vertex = min(vertex1, vertex2)
    removed_vertex = max(vertex1, vertex2)
    
    for vertex in graph[removed_vertex]:
        graph[vertex].remove(removed_vertex)
        graph[vertex].append(super_vertex)

    # merge the vertices
    graph[super_vertex].extend(graph[removed_vertex])
    del graph[removed_vertex]

    # remove self loops
    while super_vertex in graph[super_vertex]:
        graph[super_vertex].remove(super_vertex)

    return graph


def karger_min_cut(graph):
    # graph is an adjacency list
    # len(graph) == # of vertices in graph
    while len(graph) > 2:
        edge = choose_edge(graph)
        new_graph = contract_edge(graph, edge)
        karger_min_cut(new_graph)
    return graph


def import_graph(file):
    graph = dict()
    with open(file, mode="rt", encoding="utf-8") as f:
        for line in f:
            lst = [int(s) for s in line.split()]
            graph[lst[0]] = lst[1:]
    return graph
