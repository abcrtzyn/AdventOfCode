import numpy as np

s = 1;
DPR = {}

def tiltRow(row):
    key = ''.join(list(row))
    if key in DPR:
        #print('yes, its working')
        return DPR[key]
    O_count = 0;
    for i in range(row.shape[0]):
        if row[i] == '#':
            for j in range(1,O_count+1):
                row[i-j] = 'O'
            O_count=0
        elif row[i] == 'O':
            O_count+=1;
            row[i] = '.'
    for j in range(1,O_count+1):
        row[-j] = 'O'
    
    DPR[key] = list(row)
    return row

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

def tiltGrid(grid, dire):
    if dire == NORTH:
        for i in range(s):
            grid[::-1,i] = tiltRow(grid[::-1,i])
    elif dire == SOUTH:
        for i in range(s):
            grid[::1,i] = tiltRow(grid[::1,i])
    elif dire == WEST:
        for i in range(s):
            grid[i,::-1] = tiltRow(grid[i,::-1])
    elif dire == EAST:
        for i in range(s):
            grid[i,::1] = tiltRow(grid[i,::1])
    
    return grid


def spinCycle(grid):
    grid = tiltGrid(tiltGrid(tiltGrid(tiltGrid(grid,NORTH),WEST),SOUTH),EAST)
    return grid

with open('Day14/input.txt') as f:
    grid = np.array([list(x.strip()) for x in f.readlines()])
    s = grid.shape[0]

DPG = {}

i = 0
#st = ''.join(grid.flatten())
grids = list()

key = ''
while i < 1000:

    grids.append(''.join(grid.flatten()))
    
    spinCycle(grid)
    i += 1;
    
    if ''.join(grid.flatten()) in grids:
        break


print('found a match')
print(i,grids.index(''.join(grid.flatten())))
# so at 155, go to 92
from textwrap import wrap

fin = np.array([list(x) for x in wrap(grids[(1000000000-155)%63+92], s)])


# calculate score
acc = 0
for i in range(s):
    acc += (s-i)*(fin[i,:]=='O').sum()

print(acc)


#\operatorname{mod}\left(x-155,63\right)+92


# while i < 1000000000:
#     key = DPG[key]
#     i += 1


# print(i)

#print(grid)