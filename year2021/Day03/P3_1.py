mostcommon = 0
leastcommon = 0
import numpy as np
with open("input.txt", "r") as f:
    lines = f.readlines()
    ints = [[int(c) for c in list(s) if c != "\n"] for s in lines]
    arr = np.array(ints)
    sums = arr.sum(0)
    for s in sums:
        if s > 500:
            mostcommon += 1
        else:
            leastcommon += 1
        mostcommon = mostcommon << 1
        leastcommon = leastcommon << 1

print(mostcommon >> 1)
print(leastcommon >> 1)
print((mostcommon >> 1) * (leastcommon >> 1))