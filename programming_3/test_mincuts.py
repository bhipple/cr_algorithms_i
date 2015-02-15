#!/usr/bin/python
import unittest
from mincuts import *
from copy import *
import pdb

def readGraphFromFile(filePath):
    fh = open(filePath)
    G = Graph()
    for line in fh:
        parts = line.split()
        v = Vertex(parts[0])
        for i in range(1, len(parts)):
            v.adj.append(parts[i])

        G.nodes.append(v)

    return G

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.G1 = readGraphFromFile('unit.txt')

    def test_meld(self):
        G = deepcopy(self.G1)
        G.meldVertices(G.getByName('1'), G.getByName('2'))

        self.assertEqual(4, G.getEdgeCount())
        self.assertEqual(2, len(G.nodes))

    def test_edgecount(self):
        self.assertEqual(6, self.G1.getEdgeCount())

    def test_getByName(self):
        self.assertTrue('2' in self.G1.getByName('2').names)

    def test_getNotByName(self):
        self.assertFalse('1' in self.G1.getByName('2').names)

    def test_minCuts(self):
        self.assertEqual(2, minCutSim(self.G1, 100))

    def test_getIthEdge(self):
        self.assertTrue('1' in self.G1.nodeNamesAtIthEdge(0))
        self.assertTrue('2' in self.G1.nodeNamesAtIthEdge(0))
        self.assertTrue('1' in self.G1.nodeNamesAtIthEdge(1))
        self.assertTrue('3' in self.G1.nodeNamesAtIthEdge(1))
        self.assertTrue('2' in self.G1.nodeNamesAtIthEdge(2))
        self.assertTrue('1' in self.G1.nodeNamesAtIthEdge(2))
        self.assertTrue('2' in self.G1.nodeNamesAtIthEdge(3))
        self.assertTrue('3' in self.G1.nodeNamesAtIthEdge(3))
        self.assertTrue('1' in self.G1.nodeNamesAtIthEdge(4))
        self.assertTrue('3' in self.G1.nodeNamesAtIthEdge(4))
        self.assertTrue('2' in self.G1.nodeNamesAtIthEdge(5))
        self.assertTrue('3' in self.G1.nodeNamesAtIthEdge(5))

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.G1 = readGraphFromFile('rectangle_two_cuts.txt')

    def test_edgecount(self):
        self.assertEqual(28, self.G1.getEdgeCount())

    def test_minCuts(self):
        self.assertEqual(2, minCutSim(self.G1, 100))

class TestMagic(unittest.TestCase):
    def setUp(self):
        self.G1 = readGraphFromFile('magic_three_cuts.txt')

    def test_minCuts(self):
        self.assertEqual(3, minCutSim(self.G1, 100))


test_mode = False
if __name__ == '__main__':
    if test_mode:
        unittest.main()
    else:
        G = readGraphFromFile('kargerMinCut.txt')
        print "And the answer is:"
        print minCutSim(G, 500)
