# we are assured that the path has no branches
import numpy as np
from itertools import combinations



with open('Day20/input.txt') as f:
    grid = np.array([list(line.strip()) for line in f.readlines()])

path = np.zeros(grid.shape,np.int16)


start_y, start_x = np.argwhere(grid == 'S')[0]
end_y, end_x = np.argwhere(grid == 'E')[0]




current_y, current_x = start_y, start_x


# get the starting direction
for dir_y,dir_x in [(0,1),(0,-1),(1,0),(-1,0)]:
    if grid[current_y+dir_y, current_x+dir_x] == '.':
        break

directions = {
    (0,1): (1,0),
    (0,-1): (1,0),
    (1,0): (0,1),
    (-1,0): (0,1)
}


path_index = 1

# trace the path
while not (current_y == end_y and current_x == end_x):
    path[current_y,current_x] = path_index
    path_index += 1

    # try move forward
    if grid[current_y+dir_y, current_x+dir_x] != '#':
        current_y += dir_y
        current_x += dir_x
        continue

    # else, try left and right
    dir_y, dir_x = directions[(dir_y,dir_x)]
    if grid[current_y+dir_y, current_x+dir_x] != '#':
        current_y += dir_y
        current_x += dir_x
        continue
    
    dir_y, dir_x = -dir_y, -dir_x
    if grid[current_y+dir_y, current_x+dir_x] != '#':
        current_y += dir_y
        current_x += dir_x
        continue

    raise Exception('could not find a valid direction to move')

# do the end square
path[current_y,current_x] = path_index

del grid

shortcuts = 0

# now for the actual important stuff
# for each 0 in the path grid, just the internal 0s, not the edges
    # look at all the numbers around it
    # any nonzero numbers that are more than two difference are a shortcut

for i in range(1,path.shape[0]-1):
    for j in range(1, path.shape[1]-1):
        if path[j,i] != 0:
            continue

        # check around it for nonzero numbers
        numbers = []
        for dy,dx in directions:
            if path[j+dy,i+dx] != 0:
                numbers.append(path[j+dy,i+dx])
        
        if len(numbers) > 1:
            for n1, n2 in combinations(numbers,2):
                diff = int(abs(n1-n2))
                if diff >= 102:
                    # it is a shortcut greater than 100
                    shortcuts += 1


print('Part 1:',shortcuts)


# for part 2, from every point on the path
# any cell that has a manhattan distance of 20 or less that saves time is a shortcut
# so
# I will check every offset of length less than and including 20

# A B C . . A B C . . .
# . . . . . . . . . . .

# A B C . . . . . . . .
# . . . . A B C . . . .

# A B C . . . . . . . .
# . . . . . . . . . . .
# . . . A B C . . . . .

# given a distance d
# the y,x offset from (0,0) is all cells (i,d-i) and (-i,d-i) from -d+1 to d
# then the porgram checks every possible pair such that (y,x) and (y+i,x+d-i) is on the grid
shortcuts2 = 0


for d in range(2,20+1):
    for i in range(-d+1,d+1):
        y_off = i
        x_off = d - abs(i)

        for y1 in range(max(-y_off,1),min(path.shape[0]-1-y_off,path.shape[0]-1)):
            y2 = y1 + y_off
            
            for x1 in range(1,path.shape[1]-1-x_off):
                x2 = x1 + x_off

                # check that both cells are not wall cells
                if path[y1,x1] == 0 or path[y2,x2] == 0:
                    continue

                # calculate the time saved
                time_saved = abs(path[y1,x1]-path[y2,x2])-d

                if time_saved >= 100:
                    shortcuts2 += 1

    # exit(0)

print('Part 2:',shortcuts2)
