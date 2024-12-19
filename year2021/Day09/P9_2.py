import numpy as np

basinSizes = list()

def searchGrid(grid, x, y):
    grid[x,y] = False
    size = 1
    if grid[x-1][y]:
        size += searchGrid(grid, x-1, y)
    if grid[x][y-1]:
        size += searchGrid(grid, x, y-1)
    if grid[x+1][y]:
        size += searchGrid(grid, x+1, y)
    if grid[x][y+1]:
        size += searchGrid(grid, x, y+1)
    return size


with open("input.txt",'r') as f:
    grid = np.array([[int(i) for i in list(s.strip())] for s in f.readlines()])
    #print(grid.shape)
    border0 = [[9] * grid.shape[1]]
    grid = np.concatenate((border0, grid, border0), axis = 0)
    border1 = [[9]] * grid.shape[0]
    grid = np.concatenate((border1, grid, border1), axis = 1)
    basinsGrid = grid != 9
    for i in range(1, basinsGrid.shape[0]-1):
        for j in range(1, basinsGrid.shape[1]-1):
            if basinsGrid[i][j]:
                basinSizes.append(searchGrid(basinsGrid, i,j))
    
basinSizes.sort()
print(basinSizes[-3:])
print(np.multiply.reduce(basinSizes[-3:]))

                
