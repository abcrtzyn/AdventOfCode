import numpy as np

total = 0
with open("input.txt",'r') as f:
    grid = np.array([[int(i) for i in list(s.strip())] for s in f.readlines()])
    #print(grid.shape)
    border0 = [[10] * grid.shape[1]]
    grid = np.concatenate((border0, grid, border0), axis = 0)
    border1 = [[10]] * grid.shape[0]
    grid = np.concatenate((border1, grid, border1), axis = 1)
    for i in range(1, grid.shape[0]-1):
        for j in range(1, grid.shape[1]-1):
            if grid[i][j] < grid[i-1][j] and grid[i][j] < grid[i+1][j] and grid[i][j] < grid[i][j-1] and grid[i][j] < grid[i][j+1]:
                total += grid[i][j] + 1
print(total)