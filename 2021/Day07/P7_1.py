import numpy as np

with open('input.txt', 'r') as f:
    pos = np.array([int(number) for number in f.readline().strip().split(',')])
    pos.sort()
    count = pos.shape[0]
    i = count//2 #turns out the solution is always the median
    print(pos[i])
    print(np.sum(np.abs(pos - pos[i])))