 
from dataclasses import dataclass, field
from typing import Dict, Iterator, Tuple
from itertools import combinations, permutations

from python_utils.graph_traversals.shortest_path import a_star


with open('Day24/input.txt') as f:
    grid = f.readlines()

# grid_size = (len(grid),len(grid[0]))



@dataclass(order=True)
class Entry:
    priority: int
    coord: Tuple[int,int]=field(compare=False)

def taxicab(a: Tuple[int,int],b: Tuple[int,int]):
    return abs(a[0]-b[0])+abs(a[1]+b[1])


directions = [(1,0),(0,1),(-1,0),(0,-1)]

def neighbors(current: Tuple[int,int],score: int) -> Iterator[Tuple[int,Tuple[int,int]]]:
    for dx, dy in directions:
            # dont have to worry about goint off the edge 
            # because the grid is all walled off
            neighbor = (current[0]+dx,current[1]+dy)
            if grid[neighbor[0]][neighbor[1]] == '#':
                continue
            
            yield 1,neighbor
        



# find the numbers
numbers = list(range(8))
number_coords: Dict[int,Tuple[int,int]] = {}


for i,line in enumerate(grid):
    for n in numbers:
        res = line.find(str(n))
        if res != -1:
            number_coords[n] = (i,res)
            numbers.remove(n)

edges: Dict[Tuple[int,int],int] = {}
# find all shortest paths from each number to each number using A*
for (a,ac),(b,bc) in combinations(number_coords.items(),2):
    #print(a,ac,b,bc)
    d = a_star(ac,bc,neighbors,taxicab)
    if d is None:
        print(ac,bc,'no path')
        exit(1)
    #print(a,ac,b,bc,d)
    edges[(a,b)] = d
    edges[(b,a)] = d
    # exit(0)

#print(edges)

# now figure out the travelling salesman problem
min_dist = 10000
min_tour = 10000
for tour in permutations(range(1,8)):
    tour = [0] + list(tour)
    
    # PART 1
    dist = sum(edges[(tour[i], tour[i-1])] for i in range(1,len(tour)))
    if dist < min_dist:
        min_dist = dist
    # PART 2
    tour = sum(edges[(tour[i], tour[i-1])] for i in range(0,len(tour)))
    if tour < min_tour:
        min_tour = tour

print('Part 1:',min_dist)
print('Part 2:',min_tour)
# print(edges)
