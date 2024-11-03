with open('Day10/input.txt') as f:
    grid = [x.strip() for x in f.readlines()]

a = 0;
b = 0;
for line, idx in zip(grid,range(len(grid))):
    b = line.find('S');
    if(b != -1):
        a = idx;
        break;

print(a, b)

NORTH = [-1,0]
SOUTH = [1,0]
EAST = [0,1]
WEST = [0,-1]



# from the starting point, figure out the two valid connections
# manually done
point_x = a
point_y = b
dire = WEST

from time import sleep

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
            print(i/2)
            break
        case _:
            raise Exception(grid[point_x][point_y])
