# I could not come up with this on my own originally.
# the problem is calculating the area inside a figure
# The method I had seen was (for each '.', it is inside if the number of pipes to the edge is even or odd)
# I am going to do similar, while in the loop, keep track of the parity as I go.

# SETUP
# make an array that shows all cells that are a part of the loop
# replace the S with what it should be
# replace all non-loop characters with '.'

# 
# for each line
#       change the inside outside parity if '|', 'F---J', 'L---7' are present. 
#       Count '.' if inside


import numpy as np

with open('Day10/input.txt') as f:
    grid = np.array([list(x.strip()) for x in f.readlines()])

NORTH = [-1,0]
SOUTH = [1,0]
EAST = [0,1]
WEST = [0,-1]


a,b = np.where(grid == 'S')



point_x = int(a[0])
point_y = int(b[0])

# from the starting point, figure out one of the two valid connections to start
def start_direction(x,y):
    check_x = x+NORTH[0]
    check_y = y+NORTH[1]

    if str(grid[check_x,check_y]) in '|F7':
        # NORTH is valid
        return NORTH
    
    check_x = x+SOUTH[0]
    check_y = y+SOUTH[1]
    if str(grid[check_x,check_y]) in '|LJ':
        # NORTH is valid
        return SOUTH

    check_x = x+EAST[0]
    check_y = y+EAST[1]
    if str(grid[check_x,check_y]) in '-J7':
        # NORTH is valid
        return EAST

    raise AssertionError('start_direction unreachable')


start_dire = start_direction(point_x,point_y)
dire = start_dire

# trace the loop marking all spots that are part of the loop
loop = np.zeros((len(grid),len(grid[0])),bool)
loop[point_x,point_y] = 1;
while True:
    point_x = point_x + dire[0]
    point_y = point_y + dire[1]
    # mark the new point as loop
    loop[point_x,point_y] = 1;

    match grid[point_x,point_y]:
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

# clean up the grid
grid[np.logical_not(loop)] = '.'
del loop

# replace S with what it should be
if start_dire == NORTH and dire == NORTH:
    grid[point_x,point_y] = '|'
elif start_dire == NORTH and dire == EAST:
    grid[point_x,point_y] = 'J'
elif start_dire == NORTH and dire == WEST:
    grid[point_x,point_y] = 'L'
elif start_dire == SOUTH and dire == SOUTH:
    grid[point_x,point_y] = '|'
elif start_dire == SOUTH and dire == EAST:
    grid[point_x,point_y] = '7'
elif start_dire == SOUTH and dire == WEST:
    grid[point_x,point_y] = 'F'
elif start_dire == EAST and dire == EAST:
    grid[point_x,point_y] = '-'
elif start_dire == EAST and dire == NORTH:
    grid[point_x,point_y] = 'F'
elif start_dire == EAST and dire == SOUTH:
    grid[point_x,point_y] = 'L'
else:
    raise Exception('the starting direction is west or the ending direction doesn\'t make sense')

columns = grid.shape[1]

in_flag = False
ins = 0

for i in range(grid.shape[0]):
    j = 0
    if in_flag:
        raise Exception('in_flag is true at the end of a row')
    while j < columns:
        c = grid[i,j]
        if c == '.':
            # if it is not a loop cell, if the inflag is set, count it
            if in_flag:
                ins += 1
        elif c == '|':
            # vertical bar switches in/out
            in_flag = not in_flag
        elif c == 'F':
            # switch inflag if the path continues up
            # loop until not '-'
            j += 1
            while grid[i,j] == '-':
                j += 1
            c = grid[i,j]
            if c == 'J':
                in_flag = not in_flag
            elif c == '7':
                pass
            else:
                raise Exception('unknown character after F--')
        elif c == 'L':
            # switch inflag if the path continues down
            # loop until not '-'
            j += 1
            while grid[i,j] == '-':
                j += 1
            c = grid[i,j]
            if c == '7':
                in_flag = not in_flag
            elif c == 'J':
                pass
            else:
                raise Exception('unknown character after L--')
        
        j += 1

print('Part 2:',ins)

# this outputs the clean loop with none of the other junk characters
# np.savetxt('Day10/clean.txt',grid,fmt='%c',delimiter='')
