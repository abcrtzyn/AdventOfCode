with open('Day10/input.txt') as f:
    grid = [x.strip() for x in f.readlines()]


# directions.
NORTH = [-1,0]
SOUTH = [1,0]
EAST = [0,1]
WEST = [0,-1]


# find the mouse
a = 0;
b = 0;
for line, idx in zip(grid,range(len(grid))):
    b = line.find('S');
    if(b != -1):
        a = idx;
        break;

# from the starting point, figure out one of the two valid connections to start
def start_direction(x,y):
    check_x = a+NORTH[0]
    check_y = b+NORTH[1]
    if grid[check_x][check_y] in '|F7':
        # NORTH is valid
        return NORTH
    
    check_x = a+SOUTH[0]
    check_y = b+SOUTH[1]
    if grid[check_x][check_y] in '|LJ':
        # NORTH is valid
        return SOUTH

    check_x = a+EAST[0]
    check_y = b+EAST[1]
    if grid[check_x][check_y] in '-J7':
        # NORTH is valid
        return EAST

    raise AssertionError('start_direction unreachable')



dire = start_direction(a,b)
point_x = a
point_y = b

# one might move in both directions until they meet.
# I will go until S is reached and half the length

i = 0
while True:
    point_x = point_x + dire[0]
    point_y = point_y + dire[1]
    i += 1;

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
            # done
            break
        case '.':
            raise AssertionError('You may have ended up with a case where S has more than two valid connections, and the program choose the one that leads nowhere, sorry')
        case _:

            raise AssertionError('Unknown char at',grid[point_x][point_y])

print('Part 1:',i/2)
