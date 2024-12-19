 
from dataclasses import dataclass, field
from functools import partial
import heapq
from typing import Any
from itertools import combinations, permutations


with open('Day24/input.txt') as f:
    grid = f.readlines()

# grid_size = (len(grid),len(grid[0]))



@dataclass(order=True)
class Entry:
    priority: int
    coord: Any=field(compare=False)

def taxicab(a,b):
    return abs(a[0]-b[0])+abs(a[1]+b[1])

def A_star(start, goal, h):
    gScore = {}
    gScore[start] = 0

    fScore = {}
    fScore[start] = h(start)

    open_set = [Entry(fScore[start],start)]

    while len(open_set) != 0:
        
        current = heapq.heappop(open_set).coord
        
        if current == goal:
            return (gScore[current])
        
        # for each neighbor
        for neighbor in [(current[0]-1,current[1]),(current[0]+1,current[1]),(current[0],current[1]-1),(current[0],current[1]+1)]:
            # dont have to worry about goint off the edge 
            # because the grid is all walled off
            if grid[neighbor[0]][neighbor[1]] == '#':
                continue
            
            tentative_gScore = gScore[current] + 1

            if neighbor not in gScore or tentative_gScore < gScore[neighbor]:
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor)

                if neighbor not in open_set:
                    heapq.heappush(open_set,Entry(fScore[neighbor],neighbor))

        # print(open_set)
        # if(len(open_set) > 20):
            # exit(0)
    
    return -1



# find the numbers
numbers = list(range(8))
number_coords = {}


for i,line in enumerate(grid):
    for n in numbers:
        res = line.find(str(n))
        if res != -1:
            number_coords[n] = (i,res)
            numbers.remove(n)

edges = {}
# find all shortest paths from each number to each number using A*
for (a,ac),(b,bc) in combinations(number_coords.items(),2):
    #print(a,ac,b,bc)
    d = A_star(ac,bc,partial(taxicab,bc))
    #print(a,ac,b,bc,d)
    edges[(a,b)] = d
    edges[(b,a)] = d
    # exit(0)

#print(edges)

# now figure out the travelling salesman problem
min_dist = 10000000000
min_tour = None
for tour in permutations(range(1,8)):
    tour = [0] + list(tour)
    
    # PART 1
    dist = sum(edges[(tour[i], tour[i-1])] for i in range(1,len(tour)))
    # PART 2
    dist = sum(edges[(tour[i], tour[i-1])] for i in range(0,len(tour)))
    if dist < min_dist:
        min_dist = dist
        min_tour = tour

print(min_dist, min_tour)
print(edges)
