#!/usr/bin/python
from two_sums import *
import unittest

def loadSet(filePath):
    nums = set()
    map(lambda x: nums.add(int(x)), open(filePath).readlines())
    return nums

class Tester(unittest.TestCase):
    def test_distinct(self):
        self.assertEqual(0, twoSums(loadSet('0.txt')))

    def test_2(self):
        self.assertEqual(1, twoSums(loadSet('1.txt')))

    def test_3(self):
        self.assertEqual(3, twoSums(loadSet('3.txt')))

    def test_5(self):
        self.assertEqual(5, twoSums(loadSet('5.txt')))

    def test_6(self):
        self.assertEqual(6, twoSums(loadSet('6.txt')))

    def test_hw(self):
        print twoSums(loadSet('algo1_programming_prob_2sum.txt'))

if __name__ == '__main__':
    unittest.main()
