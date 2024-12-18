import numpy as np
import heapq
from typing import Iterable, List, Dict, Tuple, Optional, Callable, Generator
from functools import partial

# I could use A* or something, I don't feel like it yet
def breadth_first_search[T](start: T, end: T, neighbors: Callable[[T,int],Generator[Tuple[int,T],None,None]]) -> Optional[int]:
    # given a start point, an end point, a function that gives all neighbors
    scores: Dict[T,int] = {start: 0}
    queue: List[Tuple[int,T]] = [(0,start)]

    while queue:
        _, current = heapq.heappop(queue)
        current_score = scores[current]

        if current == end:
            return current_score

        for neighbor_score, neighbor in neighbors(current,current_score):
            if neighbor not in scores:
                scores[neighbor] = neighbor_score
                heapq.heappush(queue,(neighbor_score,neighbor))

            elif scores[neighbor] > neighbor_score:
                print('multi score')
                print(scores[neighbor], neighbor_score)
                exit(1)
            
            elif scores[neighbor] == neighbor_score:
                # add extra parent
                pass
            
            # else not a better score, continue
        
    
    return None





# test size
# size = 7
# actual input size
size = 71

# I originally used booleans and iterated the corrupeted cells
# It was slow to linear search part 2, but not terrible
grid = np.zeros((size,size),np.int16)

startpoint = (0,0)
endpoint = (size-1,size-1)


with open('Day18/input.txt') as f:
    fall_list = [tuple([int(x) for x in line.strip().split(',')]) for line in f.readlines()]


def adjacent(threshold: int, cell: Tuple[int,int], score: int):
    for direction in [(-1,0),(1,0),(0,-1),(0,1)]:
        y = cell[0] + direction[0]
        x = cell[1] + direction[1]

        # if outside of range
        if not (0 <= y < grid.shape[0] and 0 <= x < grid.shape[1]):
            continue
        # if corrupted
        if grid[y,x] < threshold:
            continue

        yield (score + 1, (y,x))

grid.fill(len(fall_list))

for i,(x,y) in enumerate(fall_list):
    grid[y,x] = i

print('Part 1:',breadth_first_search(startpoint,endpoint,partial(adjacent,12)))


# lets do a binary search just because

left = 0
right = len(fall_list)

while True:
    current = (left + right) // 2
    if breadth_first_search(startpoint,endpoint,partial(adjacent,current)) is None:
        # lower
        right = current
    else:
        # higher
        left = current
    
    if left == right - 1:
        break

print(f'Part 2: {fall_list[left][0]},{fall_list[left][1]}')
