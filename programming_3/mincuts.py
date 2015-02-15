#!/usr/bin/python
class Vertex():
    def __init__(self, name):
        self.names = list(name)
        self.adj = list()

    def printMe(self):
        print "Cluster %s -> %s" % (self.names, self.adj)

    def meldWithOther(self, otherV):
        self.adj.append(otherV.adj)
        self.names.append(otherV.names)

class Edge():
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2


class Graph():
    def __init__(self):
        self.nodes = list()
        self.count = 0

    def printMe(self):
        for node in self.nodes:
            node.printMe()

    def getByName(self, name):
        matching = [n for n in self.nodes if name in n.names]
        return matching[0]

    def addNode(self, V):
        self.nodes.append(V)
        self.count += len(V.adj)

    def runMinCut(self):
        print "wip"

    def meldVertices(self, A, B):
        A.meldWithOther(B)

def readGraphFromFile(filePath):
    fh = open(filePath)
    G = Graph()
    for line in fh:
        parts = line.split()
        v = Vertex(parts[0])
        for i in range(1, len(parts)):
            v.adj.append(parts[i])

        G.addNode(v)

    return G

#def minCuts(G, trials):


if __name__ == '__main__':
    G = readGraphFromFile('unit.txt')
    G.printMe()
