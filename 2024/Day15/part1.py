from typing import List
import numpy as np

grid_chars: List[List[str]] = []


def attempt_move(grid,cy,cx,dy,dx):
    search_y = cy
    search_x = cx
    while True:
        search_y += dy
        search_x += dx

        match grid[search_y,search_x]:
            case '.':
                # commence move
                # every cell from here to cy,cx is a box
                # all of them get shifted
                grid[search_y,search_x] = 'O'
                grid[cy+dy,cx+dx] = '@'
                grid[cy,cx] = '.'
                return (cy+dy,cx+dx)
            case 'O':
                continue
            case '#':
                # no move occurs
                return cy,cx
            case _:
                raise ValueError('unreachable code in attempt_move')
    
    # add dx,dy to cx,cy
    # if it is empty, move
    # if it is a box, keep checking
    # if it is a wall, no move occurs



with open('Day15/input.txt') as f:
    while True:
        line = f.readline().strip()
        if line == '':
            break
        
        grid_chars.append(list(line))

    grid = np.array(grid_chars)

    current_y, current_x = np.argwhere(grid == '@')[0]

    # iterate through the rest of the file, the arrows
    
    while True:
        c = f.read(1)

        match c:
            case '':
                break
            case '\n':
                continue
            case '^':
                current_y,current_x = attempt_move(grid,current_y,current_x,-1,0)
            case 'v':
                current_y,current_x = attempt_move(grid,current_y,current_x,1,0)
            case '<':
                current_y,current_x = attempt_move(grid,current_y,current_x,0,-1)
            case '>':
                current_y,current_x = attempt_move(grid,current_y,current_x,0,1)
            case _:
                raise Exception('unknown case',c)
        


print('Part 1:', sum(100*x+y for x,y in np.argwhere(grid == 'O')))
