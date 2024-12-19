import numpy as np

with open('Day16/input.txt') as f:
    grid = np.array([list(x.strip()) for x in f.readlines()])



DOWN = (1, 0)
UP = (-1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
left_mirror = {UP: LEFT, DOWN: RIGHT, LEFT: UP, RIGHT: DOWN}
right_mirror = {UP: RIGHT, DOWN: LEFT, LEFT: DOWN, RIGHT: UP}


def countCells(ix,iy,id):
    energizedlr = np.zeros(grid.shape,np.bool8)
    energizedud = np.zeros(grid.shape,np.bool8)
    energizedmirrors = np.zeros(grid.shape,np.bool8)

    stack = [(ix,iy,id)]

    try:
        current = stack.pop();
        while True:
            x = current[0]
            y = current[1]
            dire = current[2]
            #print(current)
            if x < 0 or y < 0 or x >= grid.shape[0] or y >= grid.shape[1]:
                #print('index out of range')
                current = stack.pop()
                continue

            c = grid[x,y]
            #print(c)

            if c == '/':
                energizedmirrors[x,y] = True
                newdire = right_mirror[dire]
                current = (x+newdire[0],y+newdire[1],newdire)
                continue
            elif c == '\\':
                energizedmirrors[x,y] = True
                newdire = left_mirror[dire]
                current = (x+newdire[0],y+newdire[1],newdire)
                continue

            # if it is energized in the direction, grab the next thing in the stack
            # else, energize in that direction
            if dire == RIGHT or dire == LEFT:
                if energizedlr[x,y]:
                    current = stack.pop()
                    continue
                energizedlr[x,y] = True
            else:
                if energizedud[x,y]:
                    current = stack.pop()
                    continue
                energizedud[x,y] = True


            if c == '.':
                current = (x+dire[0],y+dire[1],dire)
            elif c == '|':
                if dire == RIGHT or dire == LEFT:
                    # split
                    stack.append((x+1,y,DOWN))
                    stack.append((x-1,y,UP))
                    current = stack.pop()
                    continue
                else:
                    # just like .
                    current = (x+dire[0],y+dire[1],dire)
            elif c == '-':
                if dire == UP or dire == DOWN:
                    # split
                    stack.append((x,y+1,RIGHT))
                    stack.append((x,y-1,LEFT))
                    current = stack.pop()
                    continue
                else:
                    # just like .
                    current = (x+dire[0],y+dire[1],dire)

    except IndexError:
        pass

    return np.sum(np.logical_or(np.logical_or(energizedlr,energizedud),energizedmirrors))

m = 0
s = grid.shape[0]

for i in range(s):
    m = max(m,countCells(0,i,DOWN))
    m = max(m,countCells(9,i,UP))
    m = max(m,countCells(i,0,RIGHT))
    m = max(m,countCells(i,9,LEFT))

print(m)