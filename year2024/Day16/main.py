from typing import Set, Tuple, List
from graph_traversals.breadth_first_search import breadth_first_search_parents
import numpy as np

# an intersting search problem where turning is costly

# take the first cell in the priority queue, lowest current score
# try all possible movements (forward 1, rotate right forward 1001, rotate left forward 1001)
# for part 2, im deciding to do turns seperately (forward, turn right, turn left)

NORTH = (-1,0)
EAST = (0,1)
SOUTH = (1,0)
WEST = (0,-1)

def search_directions(y,x):
    if y == 0:
        return [NORTH,SOUTH]
    elif x == 0:
        return [EAST,WEST]
    else:
        raise ValueError('expected a proper direction')


# setup the grid
with open('Day16/input.txt') as f:
    grid = np.array([list(line.strip()) for line in f])

# find S and E
startpointxy = np.argwhere(grid == 'S')[0]
startpoint = (int(startpointxy[0]),int(startpointxy[1]),EAST)
endpoint = np.argwhere(grid == 'E')[0]

def is_endpoint(point: Tuple[int,int,Tuple[int,int]]) -> bool:
    return point[0] == endpoint[0] and point[1] == endpoint[1]

def neighbors(state: Tuple[int,int,Tuple[int,int]], score: int):
    # new states are to move forward
    # and rotate
    state_y, state_x, state_dir = state

    #### forward
    next_y = state_y + state_dir[0]
    next_x = state_x + state_dir[1]
    next_dir = state_dir
    next_score = score + 1

    if grid[next_y,next_x] != '#':
        yield (next_score, (next_y, next_x, next_dir))
    
    #### rotations
    for direction in search_directions(*state_dir):
        next_y = state_y
        next_x = state_x
        next_dir = direction
        next_score = score + 1000

        yield (next_score,(next_y,next_x,next_dir))


score, parents = breadth_first_search_parents(startpoint,is_endpoint, neighbors)

print('Part 1:',score)

visited: Set[Tuple[int,int,Tuple[int,int]]] = set()

lasts: List[Tuple[int,int,Tuple[int,int]]] = []

for dy,dx in [NORTH,EAST,SOUTH,WEST]:
    if (endpoint[0],endpoint[1],(dy,dx)) in parents:
        lasts.append((int(endpoint[0]),int(endpoint[1]),(dy,dx)))

if len(lasts) > 1:
    print('help me')
    exit(1)

current = lasts[0]
# trace the graph backwards

work_queue = [current]

while len(work_queue):
    # print(work_queue)
    current = work_queue.pop()

    # keep looping on this until a branch
    # this is slightly more efficient
    while True:
        if current in visited:
            # another path has already been here
            break

        if current not in parents:
            # this is the start point
            break

        if len(parents[current]) > 1:
            work_queue += parents[current]
            break
        visited.add(current)
        current = parents[current][0]

# now convert all visited into cells

print('Part 2:', len(set([(y,x) for y,x,d in visited])))
