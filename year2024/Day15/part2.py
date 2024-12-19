from typing import List
import numpy as np

np.set_printoptions(threshold=100000,linewidth=500)

grid_chars: List[List[str]] = []


def attempt_move_left_right(grid,cy,cx,dx):
    search_x = cx
    while True:
        search_x += dx

        match grid[cy,search_x]:
            case '.':
                # commence move
                # every cell from here to cy,cx is a box
                # all of them get shifted
                while True:
                    if search_x == cx:
                        grid[cy,search_x] = '.'
                        break
                    grid[cy,search_x] = grid[cy,search_x-dx]
                    search_x -= dx
                
                return (cy,cx+dx)
            # depending of left right movement, one of the next two is an error
            case '[':
                continue
            case ']':
                continue
            case '#':
                # no move occurs
                return cy,cx
            case _:
                raise ValueError('unreachable code in attempt_move_left_right')

# given a box, left or right side, direction of movement
# determines if that box can move
# recursive function
def is_movable(grid,cy,cx,dy):

    if grid[cy,cx] == '[':
        second_x = cx + 1
    elif grid[cy,cx] == ']':
        second_x = cx - 1
    else:
        raise ValueError('expected a box, saw', grid[cy,cx])

    movable = True

    for search_x in [cx,second_x]:
        # check cx and second_x
        match grid[cy+dy,search_x]:
            case '.':
                continue
            case '#':
                movable = False
            case '[':
                movable = movable and is_movable(grid,cy+dy,search_x,dy)
            case ']':
                # if grid[cy,cx] == ']':
                    # this will have already been checked by previous
                    # no need to check again
                    # continue
                movable = movable and is_movable(grid,cy+dy,search_x,dy)
            case _:
                raise ValueError('unreachable code in is_movable')
    
    return movable


def move_up_down(grid,cy,cx,dy):
    # move a bunch of boxes
    # use is_movable to determine if it can be moved, this function assumes it can
    match grid[cy+dy,cx]:
        case '.':
            grid[cy+dy,cx] = grid[cy,cx]
            grid[cy,cx] = '.'
        case '[':
            move_up_down(grid,cy+dy,cx,dy)
            move_up_down(grid,cy+dy,cx+1,dy)
            grid[cy+dy,cx] = grid[cy,cx]
            grid[cy,cx] = '.'
            
        case ']':
            move_up_down(grid,cy+dy,cx-1,dy)
            move_up_down(grid,cy+dy,cx,dy)
            grid[cy+dy,cx] = grid[cy,cx]
            grid[cy,cx] = '.'
        case _:
            print(grid)
            print(grid[cy+dy,cx])
            raise ValueError('unreachable code in move_up_down')
            exit(5)




def attempt_move_up_down(grid,cy,cx,dy):
    match grid[cy+dy,cx]:
        case '.':
            move_up_down(grid,cy,cx,dy)
            # easy once cell move
            # grid[cy+dy,cx] = '@'
            # grid[cy,cx] = '.'
            return (cy+dy,cx)
        case '#':
            # easy no move
            return (cy,cx)
        
        case '[':
            if is_movable(grid,cy+dy,cx,dy):
                move_up_down(grid,cy,cx,dy)
                return (cy+dy,cx)
            return (cy,cx)
        case ']':
            if is_movable(grid,cy+dy,cx,dy):
                move_up_down(grid,cy,cx,dy)
                return (cy+dy,cx)
            return (cy,cx)
            
        case _:
            raise ValueError('unreachable code in attempt_move_up_down')




def replace_wider(c):
    match c:
        case '.':
            return ['.','.']
        case '#':
            return ['#','#']
        case 'O':
            return ['[',']']
        case '@':
            return ['@','.']
        case _:
            raise Exception('unknown replace wider char',c)

with open('Day15/input.txt') as f:
    while True:
        expanded_line = []
        line = f.readline().strip()
        if line == '':
            break
        for c in line:
            expanded_line += replace_wider(c)
        
        grid_chars.append(expanded_line)

    grid = np.array(grid_chars)

    current_y, current_x = np.argwhere(grid == '@')[0]

    # iterate through the rest of the file, the arrows
    
    # print(grid)
    i = 0 
    while True:
        i += 1
        c = f.read(1)
        # print(c)
        match c:
            case '':
                break
            case '\n':
                continue
            case '^':
                current_y,current_x = attempt_move_up_down(grid,current_y,current_x,-1)
            case 'v':
                current_y,current_x = attempt_move_up_down(grid,current_y,current_x,1)
            case '<':
                current_y,current_x = attempt_move_left_right(grid,current_y,current_x,-1)
            case '>':
                current_y,current_x = attempt_move_left_right(grid,current_y,current_x,1)
            case _:
                raise Exception('unknown case',c)
        # print(grid)
        # if i > 50:
        #     exit(0)

        
print('Part 2:', sum(100*x+y for x,y in np.argwhere(grid == '[')))
