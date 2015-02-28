#!/usr/bin/python
def addCheapestNode(G, X, A):
    candidate = None
    minSoFar = float('inf')
    for vertex in X:
        for edgepair in G[vertex]:
            if edgepair[0] not in X:
                if A[vertex]+edgepair[1] < minSoFar:
                    minSoFar = A[vertex]+edgepair[1]
                    candidate = edgepair[0]
    X.append(candidate)
    A[candidate] = minSoFar

def dijkstra(G,s):
    X = []
    A = {}
    X.append(s)
    A[s]=0
    while len(X) < len(G):
        addCheapestNode(G, X, A)
    return A

