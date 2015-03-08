#!/usr/bin/python
from median_maint import *
import unittest

def fileToList(fp):
    res = []
    map(lambda x:res.append(int(x)), open(fp).readlines())
    return res


class Tester(unittest.TestCase):
    def setUp(self):
        self.A = MedianFinder()

    def test_count(self):
        stream = fileToList('54.txt')
        self.assertEqual(0, self.A.ct())
        self.A.push(stream[0])
        self.assertEqual(1, self.A.ct())
        self.A.push(stream[0])
        self.assertEqual(2, self.A.ct())
        self.A.push(stream[1])
        self.assertEqual(3, self.A.ct())

    def test_median_incremental(self):
        stream = fileToList('54.txt')
        A = self.A
        A.push(stream[0])
        self.assertEqual(4, A.getMedian())
        A.push(stream[1])
        self.assertEqual(4, A.getMedian())
        A.push(stream[2])
        self.assertEqual(5, A.getMedian())
        A.push(stream[3])
        self.assertEqual(5, A.getMedian())
        A.push(stream[4])
        self.assertEqual(6, A.getMedian())
        A.push(stream[5])
        self.assertEqual(6, A.getMedian())
        A.push(stream[6])
        self.assertEqual(7, A.getMedian())
        A.push(stream[7])
        self.assertEqual(6, A.getMedian())
        A.push(stream[8])
        self.assertEqual(6, A.getMedian())
        A.push(stream[9])
        self.assertEqual(5, A.getMedian())

    def test_median_sum(self):
        stream = fileToList('54.txt')
        self.assertEqual(54, self.A.streamedMedianSum(stream))

    def test_median_sum_2(self):
        stream = fileToList('23.txt')
        self.assertEqual(23, self.A.streamedMedianSum(stream))

    def test_hw(self):
        stream = fileToList('Median.txt')
        print self.A.streamedMedianSum(stream)

if __name__ == '__main__':
    unittest.main()
