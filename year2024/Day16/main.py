from typing import Dict, Set, Tuple, List
import heapq
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


scores: Dict[Tuple[int,int,Tuple[int,int]],int] = {}
parents: Dict[Tuple[int,int,Tuple[int,int]],List[Tuple[int,int,Tuple[int,int]]]] = {}
# use heapq
queue: List[Tuple[int,Tuple[int,int,Tuple[int,int]]]] = []


heapq.heappush(queue,(0,startpoint))
scores[startpoint] = 0

while True:
    # print('queue', queue)
    # print('scores', scores)

    # grab the first element in the queue
    score_queue, (current_y, current_x, current_dir) = heapq.heappop(queue)
    current_score = scores[(current_y,current_x,current_dir)]
    if (current_y,current_x,current_dir) in scores and score_queue != current_score:
        # print('different scores')
        # print(score_queue,current_score)
        pass

    if current_y == endpoint[0] and current_x == endpoint[1]:
        break

    #### check in each direction
    # forward
    next_y = current_y + current_dir[0]
    next_x = current_x + current_dir[1]
    next_dir = current_dir
    next_score = scores[(current_y,current_x,current_dir)] + 1

    if grid[next_y,next_x] != '#':
        if (next_y,next_x,next_dir) not in scores:
            scores[(next_y,next_x,next_dir)] = next_score
            parents[(next_y,next_x,next_dir)] = [(current_y,current_x,current_dir)]
            heapq.heappush(queue,(next_score,(next_y,next_x,next_dir)))
        
        elif scores[(next_y,next_x,next_dir)] > next_score:
            # this path is better, assign new parent
            # print('path change, check it')
            scores[(next_y,next_x,next_dir)] = next_score
            parents[(next_y,next_x,next_dir)] = [(current_y,current_x,current_dir)]

        elif scores[(next_y,next_x,next_dir)] == next_score:
            # scores is the same, add new parent
            parents[(next_y,next_x,next_dir)].append((current_y,current_x,current_dir))


    for direction in search_directions(*current_dir):
        next_y = current_y
        next_x = current_x
        next_dir = direction
        next_score = scores[(current_y,current_x,current_dir)] + 1000

        check_y = next_y + next_dir[0]
        check_x = next_x + next_dir[1]


        if grid[check_y,check_x] != '#':
            if (next_y,next_x,next_dir) not in scores:
                # if unvisited
                scores[(next_y,next_x,next_dir)] = next_score
                parents[(next_y,next_x,next_dir)] = [(current_y,current_x,current_dir)]
                heapq.heappush(queue,(next_score,(next_y,next_x,next_dir)))

            elif scores[(next_y,next_x,next_dir)] > next_score:
                # if better score
                # print('path change, check it')
                scores[(next_y,next_x,next_dir)] = next_score
                parents[(next_y,next_x,next_dir)] = [(current_y,current_x,current_dir)]
                # heapq.heappush(queue,(next_score,(next_y,next_x,next_dir)))

            elif scores[(next_y,next_x,next_dir)] == next_score:
                # scores is the same, add new parent
                parents[(next_y,next_x,next_dir)].append((current_y,current_x,current_dir))


print('Part 1:',current_score)

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
