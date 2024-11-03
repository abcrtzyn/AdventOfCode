# i'm going to make a grid

import numpy as np

# looks like all single digit x,y coordinates
# lets just go to 1000 in the z
grid = np.zeros((10,10,500),dtype=np.uint16)
#grid = np.zeros((3,3,10),dtype=np.uint16)
from typing import List,Tuple

bricks: List[Tuple[Tuple[int,int,int],Tuple[int,int,int]]] = []

# i will need to access the bricks in increasing z order

with open('Day22/input.txt') as f:
    for line in f.readlines():
        (x1,y1,z1),(x2,y2,z2) = [[int(c) for c in l.split(',')] for l in line.strip().split('~')]
        
        bricks.append(((x1,y1,z1),(x2,y2,z2)))
        grid[x1:x2+1,y1:y2+1,z1:z2+1] = 1

zorder = sorted(bricks,key = lambda x: x[0][2])
supporting = np.zeros((len(bricks)),np.bool8)




for i,b in enumerate(zorder):
    # if there is no brick below any cell
    # check the next slice down
    (x1,y1,z1o),(x2,y2,z2o) = b
    #print(z1o)
    z1 = z1o
    z2 = z2o
    #print(grid[x1:x2+1,y1:y2+1,z1-1:z1])
    while z1 != 0 and not grid[x1:x2+1,y1:y2+1,z1-1:z1].any():
        z1 -= 1
        z2 -= 1
        #print(grid[x1:x2+1,y1:y2+1,z1-1:z1])

    # move down in grid and bricks
    grid[x1:x2+1,y1:y2+1,z1o:z2o+1] = 0
    grid[x1:x2+1,y1:y2+1,z1:z2+1] = i+1
    
    #print(i+1)
    #print(grid[:,:,z1-1:z1+1])
    # figure out which bricks support this one
    # if there is only one unique number in the slice below this one,
    # that number is supporting
    supporters = np.unique(grid[x1:x2+1,y1:y2+1,z1-1:z1])
    #print(supporters)
    if np.count_nonzero(supporters) == 1:
        #print(supporters.shape)
        if supporters.shape == (1,):
            supporting[supporters[0]-1] = True
        else:
            supporting[supporters[1]-1] = True

    #if i > 100:
    #    break
print(np.count_nonzero(supporting == False))
            
    

#print(bricks)
#print(grid)
        