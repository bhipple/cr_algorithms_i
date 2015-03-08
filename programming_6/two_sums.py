#!/usr/bin/python

# compute the number of target values t in the interval [-10000,10000] (inclusive)
# such that there are distinct numbers x,y in the input file that satisfy x+y=t.
def getTargets(start, end, nums):
    targets = set()
    for t in range(start, end):
        for key in nums:
            if not key + key == t and (t-key) in nums:
                targets.add(t)
                break
    return targets

def twoSums(nums):
    return len(getTargets(-10000, 10001, nums))
