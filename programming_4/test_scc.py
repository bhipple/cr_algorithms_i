#!/usr/bin/python
import unittest
from scc import *

def readGraphFromFile(filePath):
    fh = open(filePath)
    G = {}
    Grev = {}
    for line in fh:
        parts = line.split()
        uNum = int(parts[0])
        vNum = int(parts[1])

        if uNum in G:
            G[uNum].append(vNum)
        else:
            G[uNum] = [vNum]
        if not vNum in G:
            G[vNum] = []

        if vNum in Grev:
            Grev[vNum].append(uNum)
        else:
            Grev[vNum] = [uNum]
        if not uNum in Grev:
            Grev[uNum] = []

    return [G, Grev]

class TestTriangle(unittest.TestCase):
    def setUp(self):
        [self.G, self.Grev] = readGraphFromFile('three_triangles.txt')

    def test_sccs(self):
        res = scc(self.G, self.Grev)
        self.assertEqual([3,3,3], res)

class Test6321(unittest.TestCase):
    def setUp(self):
        [self.G, self.Grev] = readGraphFromFile('6321.txt')

    def test_sccs(self):
        res = scc(self.G, self.Grev)
        self.assertEqual([6,3,2,1], res)

class Test32221(unittest.TestCase):
    def setUp(self):
        [self.G, self.Grev] = readGraphFromFile('32221.txt')

    def test_sccs(self):
        res = scc(self.G, self.Grev)
        self.assertEqual([3,2,2,2,1], res[0:5])

if __name__ == '__main__':
    unittest.main()
