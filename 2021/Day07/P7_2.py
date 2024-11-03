import numpy as np

with open('input.txt', 'r') as f:
    pos = np.array([int(number) for number in f.readline().strip().split(',')])
    #pos.sort()
    count = pos.shape[0]
    mean = int(np.mean(pos))
    for i in range(mean-10,mean+10):
        dist = np.abs(pos - i)
        totalCost = np.sum((dist * (dist + 1)) / 2)
        print(totalCost)
