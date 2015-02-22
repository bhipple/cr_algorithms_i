#!/usr/bin/python
import sys
sys.setrecursionlimit(1000000)

visited = {}
leader = {}
finishOrder = []
s = 0

def printGraph(G):
    for n in G:
        res = str(n)
        for edge in G[n]:
            res += "," + str(edge)

        print res

def printBoth(G, Grev):
    print "G:"
    printGraph(G)
    print "\nGrev:"
    printGraph(Grev)

def getFinishOrder():
    return finishOrder

def leaderToSCCs(leader):
    sccs = {}
    for node in leader:
        if leader[node] in sccs:
            sccs[leader[node]] += 1
        else:
            sccs[leader[node]] = 1
    return sccs

def sccsToSizes(sccs):
    sizes = []
    for key in sccs:
        sizes.append(sccs[key])

    return sorted(sizes, reverse=True)

def dfs(G, i):
    global visited, leader, s, finishOrder
    visited[i] = True
    leader[i] = s

    for j in G[i]:
        if not j in visited:
            dfs(G, j)

    finishOrder.append(i)

def dfsLoop(G, seq):
    global visited, s, finishOrder
    visited.clear()
    s = 0

    for i in seq:
        if not i in visited:
            s = i
            dfs(G, i)

def scc(G, Grev):
    global finishOrder, leader
    finishOrder = []
    leader = {}

    initialSeq = range(len(G), 0, -1)
    dfsLoop(Grev, initialSeq)
    finishOrder.reverse()
    dfsLoop(G, finishOrder)

    return sccsToSizes(leaderToSCCs(leader))
