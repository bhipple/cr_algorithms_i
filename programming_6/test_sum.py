#!/usr/bin/python
from two_sums import *
import unittest

def loadSet(filePath):
    fh = open(filePath)
    nums = set()
    for line in fh:
        nums.add(int(line))
    return nums

class Tester(unittest.TestCase):
    def test_54(self):
        self.assertEqual(54, twoSums(loadSet('54.txt')))

    def test_3(self):
        self.assertEqual(3, twoSums(loadSet('3.txt')))

    def test_82(self):
        self.assertEqual(82, twoSums(loadSet('82.txt')))

    def test_hw(self):
        if False:
            nums = loadSet('algo1_programming_prob_2sum.txt')
            print twoSums(nums)

if __name__ == '__main__':
    unittest.main()
