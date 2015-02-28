#!/usr/bin/python
import unittest
from dijkstra import *

def loadGraphFromFile(fp):
    fh = open(fp)

    G = {}
    for line in fh:
        parts = line.split()
        key = int(parts[0])
        parts = parts[1:]

        edges = []
        for part in parts:
            pair = part.split(',')
            edges.append([int(pair[0]), int(pair[1])])
            if int(pair[0]) not in G:
                G[int(pair[0])] = []

        G[key] = edges
    return G


class TestSimple(unittest.TestCase):
    def test_simple(self):
        G = loadGraphFromFile('simple_graph.txt')
        A = dijkstra(G,1)

        self.assertEqual(A[1], 0)
        self.assertEqual(A[2], 3)
        self.assertEqual(A[3], 3)
        self.assertEqual(A[4], 5)

class TestLarger(unittest.TestCase):
    def test_larger(self):
        G = loadGraphFromFile('larger_graph.txt')
        A = dijkstra(G,1)

        self.assertEqual(A[1], 0)
        self.assertEqual(A[2], 2)
        self.assertEqual(A[4], 1)
        self.assertEqual(A[3], 3)
        self.assertEqual(A[5], 3)
        self.assertEqual(A[6], 6)
        self.assertEqual(A[7], 5)

class TestHW(unittest.TestCase):
    def test_hw(self):
        G = loadGraphFromFile('dijkstraData.txt')
        A = dijkstra(G,1)

        Nodes = [7,37,59,82,99,115,133,165,188,197]
        print filter(lambda x: x in Nodes, A)

if __name__ == '__main__':
    unittest.main()
