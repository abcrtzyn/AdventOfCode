#! not functional
mostcommon = 0
leastcommon = 0
import numpy as np
with open("input.txt", "r") as f:
    lines = f.readlines()
ints = [[int(c) for c in list(s) if c != "\n"] for s in lines]
arr = np.array(ints)
arr2 = arr.copy()

def mostCommonBit(arr: np.ndarray, place):
    count = len(arr)
    sums = arr.sum(0)
    if sums[place] >= count:
        return 1
    else:
        return 0



b = np.ma.mask_rowcols(arr, 0, arr[:,0] == mostCommonBit(arr,0))
print(b)