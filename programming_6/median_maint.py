#!/usr/bin/python
import heapq

class MedianFinder:
    def __init__(self):
        self.mins = []
        self.maxes = []

    def ct(self):
        return len(self.mins) + len(self.maxes)

    def fact(self, heap):
        if heap == self.mins:
            return -1
        return 1

    def getMedian(self):
        if self.ct() == 0:
            return float('inf')
        if self.ct() % 2 == 0:
            return -1 * self.mins[0]
        if len(self.mins) > len(self.maxes):
            return self.mins[0] * -1
        else:
            return self.maxes[0]

    def getSmaller(self):
        if len(self.mins) < len(self.maxes):
            return self.mins
        else:
            return self.maxes

    def getLarger(self):
        if len(self.mins) > len(self.maxes):
            return self.mins
        else:
            return self.maxes

    def rebalance(self):
        if abs(len(self.mins) - len(self.maxes)) <= 1:
            return
        x = self.getSmaller()
        y = self.getLarger()
        heapq.heappush(x, -1 * heapq.heappop(y))

    def push(self, x):
        if x < self.getMedian():
            heapq.heappush(self.mins, -1 * x)
        else:
            heapq.heappush(self.maxes, x)
        self.rebalance()

    def streamedMedianSum(self, seq):
        res = 0
        for i in seq:
            self.push(i)
            res += self.getMedian()
            res = res % 10000
        return res
