# this will be easiest looking at pairs of characters
# so first is data conversion

from typing import Dict, List, Set, Tuple
from itertools import combinations



antennas: Dict[str,List[Tuple[int,int]]] = {}


with open('Day08/input.txt') as f:
    grid = [x.strip() for x in f.readlines()]
    height = len(grid)
    width = len(grid[0])

    for i,line in enumerate(grid):
        for j,c in enumerate(line):
            if c != '.':
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append((i,j))

# print(antennas)

antinodes: Set[Tuple[int,int]] = set()
# now, for each character, find antinodes
for k,ant in antennas.items():
    # for each combination of points
    for p1,p2 in combinations(ant,2):
        ydiff = p1[0] - p2[0]
        xdiff = p1[1] - p2[1]

        while True:
            if 0 <= p1[0] < height and 0 <= p1[1] < width:
                antinodes.add(p1)
            else:
                # outside the map, done with this direction
                break
            
            p1 = (p1[0]+ydiff,p1[1]+xdiff)

        
        while True:
            if 0 <= p2[0] < height and 0 <= p2[1] < width:
                antinodes.add(p2)
            else:
                break

            p2 = (p2[0]-ydiff,p2[1]-xdiff)
            



print('Part 2:',len(antinodes))
    
