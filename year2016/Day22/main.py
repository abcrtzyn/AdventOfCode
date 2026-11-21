# viable pairs
# number of pairs to check about 1000^2 = about 1,000,000
# good enough for brute force

from functools import partial
from io import TextIOWrapper
from typing import Iterator, Tuple, Dict
import re

from python_utils.graph_traversals.shortest_path import a_star

line_rule = re.compile('/dev/grid/node-x(\\d+)-y(\\d+) +(\\d+)T +(\\d+)T +(\\d+)T +(\\d+)%')

grid: Dict[Tuple[int,int],Tuple[int,int,int]] = {}
SIZE = 0
USED = 1
AVAL = 2

empty: Tuple[int,int] = (0,0)
last_column = 0

def read_lines(f: TextIOWrapper):
    while True:
        line = f.readline()
        if line == '':
            break
        yield line


with open('Day22/input.txt') as f:
    f.readline()
    f.readline()
    for line in read_lines(f):
        mat = line_rule.match(line)
        if mat is None:
            print(f'did not match "{line}"')
            exit(1)
        coord = (int(mat.group(1)),int(mat.group(2)))
        stats = (int(mat.group(3)),int(mat.group(4)),int(mat.group(5)))
        grid[coord] = stats
        if stats[USED] == 0:
            empty = coord
        if coord[0] > last_column:
            last_column = coord[0]

        # check that every cell in the top row is not a wall
        if coord[1] == 0 and stats[USED] > 100:
            print(f'node ({coord[0]},{coord[1]}) must be a normal cell for this part 2 solution.')
        

viable_count = 0

for a,ar in grid.items():
    for b,br in grid.items():
        if a == b:
            continue
        if ar[USED] == 0:
            continue
        if ar[USED] <= br[AVAL]:
            viable_count += 1

print('Part 1:',viable_count)

# so really, this just creates a grid with some barriers
# at the instructions show, there is a 5 cycle pattern
# . _ G
# . . . (0)

# . G _
# . . . (1)

# . G .
# . . _ (2)

# . G .
# . _ . (3)

# . G .
# _ . . (4)

# _ G .
# . . . (5) repeat this

# So assuming that the first row in the grid is available
# We just need to get to the cell next to the goal
# and then repeat this 5 cycle the correct number of times

def taxicab(a: Tuple[int,int],b: Tuple[int,int]):
    return abs(a[0]-b[0])+abs(a[1]+b[1])

def get_neighbors(current: Tuple[int,int], score: int) -> Iterator[Tuple[int,Tuple[int,int]]]:
    for dire in [(0,-1),(0,1),(-1,0),(1,0)]:
        neighbor = (current[0] + dire[0], current[1] + dire[1])
        if not neighbor in grid:
            continue
        if neighbor == (0,last_column):
            # I'm not going to allow the path to go onto the goal
            continue
        
        # check the stats of this one
        if grid[neighbor][USED] > 100:
            # this is a wall, effectively
            continue
        yield 1,neighbor


path_to_near_goal = a_star(empty,lambda x: x == (last_column-1,0),get_neighbors,partial(taxicab,(last_column-1,0)))
if path_to_near_goal is None:
    print('found no path from the empty cell to the goal data')
    exit()

print('Part 2:', path_to_near_goal + (last_column-1) * 5 + 1)

