
from typing import Set, Tuple
import numpy as np



with open('Day06/input.txt') as f:
    grid = np.array([list(x.strip()) for x in f])

# directions are in right turn order starting with up
directions = [(-1,0),(0,1),(1,0),(0,-1)]
# start x and start y are used for all parts, they are constants from here
start_y,start_x = np.argwhere(grid == '^')[0]
# always start up
direction = 0

y = start_y
x = start_x
marked = np.zeros(grid.shape,np.bool)

# while the current position is inside the grid
while (0 <= y < grid.shape[0]) and (0 <= x < grid.shape[1]):
    if grid[y,x] == '#':
        # go back and turn right
        y -= directions[direction][0]
        x -= directions[direction][1]
        direction = (direction + 1) % 4
    else:
        # mark and continue forward
        marked[y,x] = True
        y += directions[direction][0]
        x += directions[direction][1]

# the count of marked cells
print('Part 1:', np.count_nonzero(marked))

# PART 2 CODE

def is_loop(grid, y, x, direction):
    # in order to detect loops, keep track of each cell and the direction
    visited: Set[Tuple[int,int,int]] = set()
    # same simulation code as before
    while (y,x,direction) not in visited:
        if not ((0 <= y < grid.shape[0]) and (0 <= x < grid.shape[1])):
            # off the grid, no loop
            return False

        if grid[y,x] == '#':
            # go back and turn right
            y -= directions[direction][0]
            x -= directions[direction][1]
            direction = (direction + 1) % 4
        else:
            # mark and continue forward
            visited.add((y,x,direction))
            y += directions[direction][0]
            x += directions[direction][1]
    
    return True

# using marked cells from part 1, every cell that is on the path should be checked as an obstacle
# going through 5000 some entries is a little slow, but I would rather have the correct answer
loops = 0

# for each marked cell
for i,j in np.argwhere(marked):
    if grid[i,j] == '^':
        # skip the initial one
        continue
    # make it an obstacle
    grid[i,j] = '#'

    # figure out if there is a loop
    if is_loop(grid,start_y,start_x,0):
        # increase the counter
        loops += 1
    
    # make it not an obstacle
    grid[i,j] = '.'


print('Part 2:', loops)
