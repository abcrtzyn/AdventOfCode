from functools import partial
from typing import Tuple, cast
from python_utils.graph_traversals.shortest_path import a_star, bounded_reachability

# DESIGNERS_FAVORITE_NUMBER = 10
with open('Day13/input.txt') as f:
    DESIGNERS_FAVORITE_NUMBER = int(f.read().strip())

start = (1,1)
# goal = (7,4)
goal = (31,39)


def taxicab(a: Tuple[int,int],b: Tuple[int,int]) -> int:
    return abs(a[0]-b[0])+abs(a[1]+b[1])

# determines if a given cell is a wall
def iswall(p: Tuple[int,int]):
    n = p[0]**2 + 3*p[0] + 2 * p[0] * p[1] + p[1] + p[1]**2 + DESIGNERS_FAVORITE_NUMBER
    
    return n.bit_count() % 2


def get_neighbors(current: Tuple[int,int], score: int):
    for neighbor in [(current[0]-1,current[1]),(current[0]+1,current[1]),(current[0],current[1]-1),(current[0],current[1]+1)]:
        if neighbor[0] < 0 or neighbor[1] < 0:
            continue
        if iswall(neighbor):
            continue
        yield 1,neighbor


print('Part 1:', a_star(cast(Tuple[int,int],start),lambda x: x == goal,get_neighbors,partial(taxicab,goal)))
print('Part 2:',bounded_reachability(start,50,get_neighbors))
