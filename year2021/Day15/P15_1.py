# steps = length + width-2

# start [0,0]

import numpy as np
with open('input_test.txt', 'r') as f:
    grid = np.array([[int(i) for i in list(s.strip())] for s in f.readlines()],np.uint16)
    risk = np.zeros(grid.shape, dtype=np.int16)
    
    risk[0,0] = 0
    c = 0
    for i in range(1,2*grid.shape[0]-1):
        for j in range(i+1):
            if j >= grid.shape[0] or i-j >= grid.shape[0]:
                #print(j, i-j)
                continue #off the grid to the left or right
            c += 1
            riskJ = np.inf
            riskI = np.inf
            if j != 0:
                #check risk from j-1
                riskJ = risk[j-1,i-j]
            if i-j != 0:
                #check risk from i-j-1
                riskI = risk[j,i-j-1]
            risk[j,i-j] = min(riskI,riskJ) + grid[j,i-j]
        #print(risk)
    print(risk)
    print(risk[-1,-1])