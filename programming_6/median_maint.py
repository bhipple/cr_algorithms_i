#!/usr/bin/python
import heapq

class MedianFinder:
    def __init__(self):
        self.mins = []
        self.maxes = []

    def ct(self):
        return len(self.mins) + len(self.maxes)

    def getMedian(self):
        if self.ct() == 0:
            return float('inf')
        if self.ct() % 2 == 0:
            return -1 * self.mins[0]
        return abs(self.getLarger()[0])

    def getSmaller(self):
        if len(self.mins) < len(self.maxes):
            return self.mins, -1
        else:
            return self.maxes, 1

    def getLarger(self):
        if len(self.mins) > len(self.maxes):
            return self.mins
        else:
            return self.maxes

    def rebalance(self):
        if abs(len(self.mins) - len(self.maxes)) <= 1:
            return
        x, fact = self.getSmaller()
        y = self.getLarger()
        heapq.heappush(x, fact * heapq.heappop(y))

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
        return res


