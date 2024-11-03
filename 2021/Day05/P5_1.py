import numpy as np

grid = np.zeros((1024,1024), dtype=np.int16)

def addToGrid(x,y):
    global grid
    #print(x,y)
    grid[x][y] += 1

def parseLine(line: str):
    return tuple([tuple([int(number) for number in coord.split(',')]) for coord in line.strip().split(' -> ')])
    
with open('input.txt') as f:
    for line in f:
        #print(line)
        (x1, y1), (x2, y2) = parseLine(line)
        if x1 == x2:
            if y1 <= y2:
                for y in range(y1,y2+1):
                    addToGrid(x1,y)
            else:
                for y in range(y2,y1+1):
                    addToGrid(x1, y)
        elif y1 == y2:
            if x1 <= x2:
                for x in range(x1,x2+1):
                    addToGrid(x, y1)    
            else:
                for x in range(x2, x1+1):
                    addToGrid(x,y1)

print(np.sum(grid >= 2))

