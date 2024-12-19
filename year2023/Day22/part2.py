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
new_bricks = []

# make the bricks fall
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
    new_bricks.append(((x1,y1,z1),(x2,y2,z2)))
    
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
print()
# to look at how many bricks fall if, we only need to look at the bricks 
# that are supporting other bricks.
# i am also going to start from the top down

total_bricks = 0

for i,v in reversed(list(enumerate(supporting))):
    print('i',i)
    # if it supports no bricks
    if not v:
        continue
    
    (x1,y1,z1),(x2,y2,z2) = new_bricks[i]
    
    #print('above',grid[x1:x2+1,y1:y2+1,z2+1])

    cgrid = grid.copy()
    #cnew_bricks = [x for x in new_bricks]
    # # remove the ith brick
    cgrid[x1:x2+1,y1:y2+1,z1:z2+1] = 0

    queue = []
    # for each brick that it supports
    below = np.unique(cgrid[x1:x2+1,y1:y2+1,z2+1])
    for j in below:
        if j != 0:
            queue.append(j-1)

    while len(queue) > 0:
        didntmove = 0
        # i think i have to select the lowest z2 value
        #j = min(queue,key=lambda x: new_bricks[x][1][2])
        #queue.remove(j)
        j  = queue.pop(0)

        #print(j,end=' ')
        # move brick down
        (x1j,y1j,z1j),(x2j,y2j,z2j) = new_bricks[j]
        cgrid[x1j:x2j+1,y1j:y2j+1,z1j:z2j+1] = 0

        if not(z1j != 0 and not cgrid[x1j:x2j+1,y1j:y2j+1,z1j-1].any()):
            didntmove = 1
        else:
            while z1j != 0 and not cgrid[x1j:x2j+1,y1j:y2j+1,z1j-1].any():
                #print('movin down')
                z1j -= 1
                z2j -= 1
                #print(cgrid[x1:x2+1,y1:y2+1,z1-1:z1])
        
        cgrid[x1j:x2j+1,y1j:y2j+1,z1j:z2j+1] = j+1
        #cnew_bricks[j] = ((x1j,y1j,z1j),(x2j,y2j,z2j))

        if not didntmove:
            total_bricks += 1
            # add more bricks to the queue
            #print('above',cgrid[x1j:x2j+1,y1j:y2j+1,new_bricks[j][1][2]+1])
            below = np.unique(cgrid[x1j:x2j+1,y1j:y2j+1,new_bricks[j][1][2]+1])
            for k in below:
                if k != 0 and k-1 not in queue:
                    queue.append(k-1)

        #print(cgrid)
    #print()

    #if i < 1150:
    #    break
        
    
print('n',total_bricks)


        

    # # if there is no brick below any cell
    # # check the next slice down
    # (x1,y1,z1o),(x2,y2,z2o) = b
    # #print(z1o)
    # z1 = z1o
    # z2 = z2o
    # #print(grid[x1:x2+1,y1:y2+1,z1-1:z1])
    # while z1 != 0 and not grid[x1:x2+1,y1:y2+1,z1-1:z1].any():
    #     z1 -= 1
    #     z2 -= 1
    #     #print(grid[x1:x2+1,y1:y2+1,z1-1:z1])

    # # move down in grid and bricks


            
    

#print(bricks)
#print(grid)
        