# I could not come up with this on my own.
import numpy as np

with open('Day10/input.txt') as f:
    grid = np.array([list(x.strip()) for x in f.readlines()])

NORTH = [-1,0]
SOUTH = [1,0]
EAST = [0,1]
WEST = [0,-1]



# from the starting point, figure out the two valid connections
# manually done
point_x = 62
point_y = 61
dire = WEST

loop = np.zeros((len(grid),len(grid[0])),bool)
loop[point_x][point_y] = 1;
while True:
    point_x = point_x + dire[0]
    point_y = point_y + dire[1]
    # mark the new point as loop
    loop[point_x][point_y] = 1;


    match grid[point_x][point_y]:
        case '-':
            pass
        case '|':
            pass
        case 'F':
            if dire == WEST:
                dire = SOUTH
            else:
                dire = EAST
        case 'J':
            if dire == SOUTH:
                dire = WEST
            else:
                dire = NORTH
        case 'L':
            if dire == WEST:
                dire = NORTH
            else:
                dire = EAST
        case '7':
            if dire == NORTH:
                dire = WEST
            else:
                dire = SOUTH
        case 'S':
            break
        case _:
            raise Exception(grid[point_x][point_y])

import re


fjpat = re.compile('F-*J')
l7pat = re.compile('L-*7')

def trace(s: str) -> int:
    pipe = s.count('|')
    fj = len(fjpat.findall(s))
    l7 = len(l7pat.findall(s))
    return pipe + fj + l7

ins = 0
# for each cell that is not a loop, count pipes between point and the left edge
# if that is even, outside; if odd, inside
for i in range(loop.shape[0]):
    for j in range(loop.shape[1]):
        if loop[i][j] == 1:
            continue
        if j==0:
            continue
        pertinant_range = grid[i][0:j];
        filt = pertinant_range[loop[i][0:j]]
        if len(filt) == 0:
            continue
        #if j == 139:
            #print(str.join('',list(filt)))
        ins += trace(str.join('',list(filt))) % 2
        
    
print(ins)
