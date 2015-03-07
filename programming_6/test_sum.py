#!/usr/bin/python
from two_sums import *
import unittest

def loadDict(filePath):
    fh = open(filePath)
    nums = {}
    for line in fh:
        num = int(line)
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 1
    return nums

class Tester(unittest.TestCase):
    def test_load(self):
        d = loadDict('82.txt')
        self.assertEqual(1, d[1])
        self.assertEqual(2, d[4])
        self.assertEqual(1, d[-4])

    def test_54(self):
        self.assertEqual(54, twoSums(loadDict('54.txt')))

    def test_3(self):
        self.assertEqual(3, twoSums(loadDict('3.txt')))

    def test_82(self):
        self.assertEqual(82, twoSums(loadDict('82.txt')))

    def disable(self):
        nums = loadDict('algo1_programming_prob_2sum.txt')
        print twoSums(nums)

if __name__ == '__main__':
    unittest.main()
