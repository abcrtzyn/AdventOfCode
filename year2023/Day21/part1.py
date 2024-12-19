# make a grid
import numpy as np

with open('Day21/input.txt') as f:
    grid = np.array([[(y=='#') for y in x.strip()] for x in f.readlines()])

#print(grid)

start = (65,65)
#start = (5,5)
queue = [(0,start)]

# at step 0, always on even,even or odd,odd parity
# 64 steps will have the same parity
steps = np.zeros(grid.shape,np.bool8)

i = 0
while len(queue) != 0:
    curstep, (starty,startx) = queue.pop(0)
    if steps[starty,startx]:
        continue
    #print(curstep,starty,startx)#, steps[starty,startx])
    
    steps[starty,startx] = True
    if curstep == 64:
        continue
    # if not already in steps, add the four directions to the queue
    if not grid[starty-1,startx] and not steps[starty-1,startx]:
        #print('adding', starty-1,startx)
        queue.append((curstep+1,(starty-1,startx)))
    if not grid[starty+1,startx] and not steps[starty+1,startx]:
        #print('adding', starty+1,startx)
        queue.append((curstep+1,(starty+1,startx)))
    if not grid[starty,startx-1] and not steps[starty,startx-1]:
        #print('adding', starty,startx-1)
        queue.append((curstep+1,(starty,startx-1)))
    if not grid[starty,startx+1] and not steps[starty,startx+1]:
        #print('adding', starty,startx+1)
        queue.append((curstep+1,(starty,startx+1)))
    i+=1
    # if(i > 1000):
    #     break
#print(i)
#print(steps.astype(np.uint8))

# now, count all of the even even and odd odd squares
# because of the shape, i can flatten and count every other cell
print(np.count_nonzero(steps.flatten()[::2]))