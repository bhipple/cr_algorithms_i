#!/usr/bin/python
from random import *
from copy import *

class Vertex():
    def __init__(self, name):
        self.names = list()
        self.names.append(name)
        self.adj = list()

    def printMe(self):
        print "Cluster %s -> %s" % (self.names, self.adj)

    def meldWithOther(self, otherV):
        self.adj.extend(otherV.adj)
        self.names.extend(otherV.names)

        # Eliminate self loops
        self.adj = filter(lambda e : not (e in otherV.names or e in self.names), self.adj)

class Graph():
    def __init__(self):
        self.nodes = list()

    def printMe(self):
        map(lambda x : x.printMe(), self.nodes)

    def getByName(self, name):
        matching = [n for n in self.nodes if name in n.names]
        return matching[0]

    def popByName(self, node):
        for name in node.names:
            for i in range(len(self.nodes)):
                if name in self.nodes[i].names:
                    self.nodes.pop(i)
                    return

    def getEdgeCount(self):
        return sum(map(lambda x : len(x.adj), self.nodes))

    def nodeNamesAtIthEdge(self, i):
        ct = 0
        for node in self.nodes:
            for e in node.adj:
                if ct == i:
                    return node.names[0], e
                ct += 1

    def crossEdges(self):
        if not len(self.nodes) == 2:
            print "Didn't reduce the graph?"
            return

        clusterEdges = self.nodes[0].adj
        clusterNames = self.nodes[0].names

        return len(filter(lambda x : x not in clusterNames, clusterEdges))

    def meldVertices(self, A, B):
        self.popByName(B)
        A.meldWithOther(B)

def minCut(G):
    while len(G.nodes) > 2:
        e = randint(0, G.getEdgeCount()-1)
        [A, B] = G.nodeNamesAtIthEdge(e)
        G.meldVertices(G.getByName(A), G.getByName(B))

    return G.crossEdges()

def minCutSim(G_orig, trials):
    best = len(G_orig.nodes)
    for i in range(trials):
        best = min(best, minCut(deepcopy(G_orig)))
        print "Best = %s after run %s" % (best, i)
    return best
