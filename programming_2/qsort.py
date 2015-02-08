#!/usr/bin/python
import unittest

PVT = "FIRST"

# Uses a heuristic to select a pivot and move it and swap it
# with the first element in the range
def movePivot(arr, leftIdx, rightIdx):
    global PVT
    if PVT == "FIRST":
        return
    elif PVT == "LAST":
        arr[leftIdx], arr[rightIdx] = arr[rightIdx], arr[leftIdx]
    elif PVT == "MEDIAN_OF_THREE":
        a = sorted([arr[leftIdx], arr[rightIdx], arr[(leftIdx + rightIdx)/2]])
        if arr[rightIdx] == a[1]:
            arr[leftIdx], arr[rightIdx] = arr[rightIdx], arr[leftIdx]
        elif arr[(leftIdx+rightIdx)/2] == a[1]:
            arr[leftIdx], arr[(leftIdx+rightIdx)/2] = arr[(leftIdx+rightIdx)/2], arr[leftIdx]


# Uses first element in range as pivot
# Partitions in range [leftIdx, rightIdx)
def partition(arr, leftIdx, rightIdx):
    p = arr[leftIdx]
    i = leftIdx+1
    for j in range(i, rightIdx):
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i-1], arr[leftIdx] = arr[leftIdx], arr[i-1]

    return i-1

def qsort(arr, leftIdx, rightIdx):
    if not arr or rightIdx <= leftIdx:
        return 0

    movePivot(arr, leftIdx, rightIdx - 1)
    p = partition(arr, leftIdx, rightIdx)
    comparisons = (rightIdx - leftIdx - 1)

    comparisons += qsort(arr, leftIdx, p)
    comparisons += qsort(arr, p+1, rightIdx)

    return comparisons

def quicksort(arr):
    return qsort(arr, 0, len(arr))


class Tester(unittest.TestCase):
    def runTest(self):
        global PVT
        A = [3, 9, 8, 4, 6, 10, 2, 5, 7, 1]

        PVT = "FIRST"
        self.assertEqual(25, quicksort(list(A)))

        PVT = "LAST"
        self.assertEqual(29, quicksort(list(A)))

        PVT = "MEDIAN_OF_THREE"
        self.assertEqual(21, quicksort(list(A)))

if __name__ == '__main__':
    print "Homework answers:"
    FH = open('QuickSort.txt')
    hw = []
    for line in FH:
        hw.append(int(line))

    PVT = "FIRST"
    print quicksort(list(hw))
    PVT = "LAST"
    print quicksort(list(hw))
    PVT = "MEDIAN_OF_THREE"
    print quicksort(list(hw))

    unittest.main()
