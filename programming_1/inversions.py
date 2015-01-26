#!/usr/bin/python

def loadArray():
    fh = open('IntegerArray.txt')

    res = []
    for line in fh:
        res.append(int(line))
    return res

def merge(a, b):
    c = []
    splitInverts = 0
    aIdx = 0
    bIdx = 0

    while aIdx < len(a) and bIdx < len(b):
        if a[aIdx] <= b[bIdx]:
            c.append(a[aIdx])
            aIdx += 1
        else:
            c.append(b[bIdx])
            bIdx += 1
            splitInverts += (len(a) - aIdx)
    while aIdx < len(a):
        c.append(a[aIdx])
        aIdx += 1
    while bIdx < len(b):
        c.append(b[bIdx])
        bIdx += 1

    return [c, splitInverts]

def inversions(arr):
    if len(arr) <= 1:
        return [arr, 0]

    [a, leftInversions] = inversions(arr[0:len(arr)/2])
    [b, rightInversions] = inversions(arr[len(arr)/2:])
    [c, splitInversions] = merge(a, b)

    return [c, leftInversions + rightInversions + splitInversions]

# MAIN
#print inversions([1, 3, 5, 2, 4, 6])
#print inversions([1,2,3,4])
#print inversions([4,3,2,1])

[a, res] = inversions(loadArray())
print res
