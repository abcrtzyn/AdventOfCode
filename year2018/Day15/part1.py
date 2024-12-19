# Grid. 0 is wall, 1 is open, anything else is a unit, dividing point set by the parser

from typing import Any, List, Tuple


grid: List[List[int]] = []

def manhattan(a,b,c,d):
    return abs(a-c) + abs(b-d)



# PARSING
units = []
goblins = 0
elves = 0

with open('Day15/input.txt') as f:
    txt = f.read()
    g = txt.count('G')
    e = txt.count('E')
    GOBLINS = 0
    ELVES = g
    WALL = g+e
    EMPTY = g+e+1
    units: List[Tuple[int,int,int]] = [None]*(g+e) #type:ignore

    f.seek(0,0)
    for j,line in enumerate(f):
        l:Any = list(line)
        for i in range(len(l)):
            match l[i]:
                case '#':
                    l[i] = WALL
                case '.':
                    l[i] = EMPTY
                case 'G':
                    l[i] = goblins
                    units[goblins] = (j,i,200)
                    goblins += 1
                case 'E':
                    l[i] = g+elves
                    units[g+elves] = (j,i,200)
                    elves += 1
                case '\n':
                    pass
                case _:
                    print(l[i])
                    exit(1)
        grid.append(l[:-1])



def square_next_to_elf(grid,y,x):
    for y_off,x_off in [(-1,0),(1,0),(0,-1),(0,1)]:
        tile = grid[y+y_off][x+x_off]
        if ELVES <= tile < WALL:
            return True
    return False

def square_next_to_goblin(grid,y,x):
    for y_off,x_off in [(-1,0),(1,0),(0,-1),(0,1)]:
        tile = grid[y+y_off][x+x_off]
        if GOBLINS <= tile < ELVES:
            return True
    return False



# find the closest square that satisfies a given predicate function
# tests all squares of a given distance, in reading order, and returns the closest one
def breadth_first_seach(grid, start_y, start_x, f):
    # it is going to be better to just compare distances and then after sort by reading order
    search = set()
    search.add((start_y,start_x))
    searched = set()
    satisfies = set()
    
    while len(satisfies) == 0:
        next_search = set()
        # print(search)
        for cell_y,cell_x in search:
            if f(grid,cell_y,cell_x):
                satisfies.add((cell_y,cell_x))
                continue
            elif len(satisfies) > 0:
                continue # shortcuts if at least one satisfies
            searched.add((cell_y,cell_x))
            # add each neighbor to next_search
            for y_off,x_off in [(-1,0),(1,0),(0,-1),(0,1)]:
                if (cell_y+y_off,cell_x+x_off) not in searched and grid[cell_y+y_off][cell_x+x_off] == EMPTY:
                    next_search.add((cell_y+y_off,cell_x+x_off))

        search = next_search
    
    print(satisfies)
    if len(satisfies) == 1:
            return satisfies.pop()
    else:
        print('multiple satisfies')
        exit(1)
    
    
    








# since wer are counting the number of rounds completed, the couter will increase at the end of the loop
rounds_completed = 0

while True:
    for (unit_y,unit_x,unit_hp) in sorted(units):
        unit_id = grid[unit_y][unit_x]
        print(unit_y,unit_x,unit_id)
        # check if next to an enemy
        if not (grid[unit_y][unit_x-1] < WALL or grid[unit_y][unit_x+1] < WALL or grid[unit_y-1][unit_x] < WALL or grid[unit_y+1][unit_x] < WALL):
            print('not next to enemy, commence move')
            
            # breadth first search to find the closest, reading order square
            if unit_id < ELVES: # is goblin
                breadth_first_seach(grid,unit_y,unit_x,square_next_to_elf)
            else:
                breadth_first_seach(grid,unit_y,unit_x,square_next_to_goblin)
        
        


    rounds_completed += 1
    exit(0)


print(rounds_completed)
print(units)
