# implementating A* for this task

from functools import partial
import heapq
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Entry:
    priority: int
    coord: Any=field(compare=False)


#DESIGNERS_FAVORITE_NUMBER = 10
DESIGNERS_FAVORITE_NUMBER = 1352

start = (1,1)
#goal = (7,4)
goal = (31,39)

# taxicab distance
def taxicab(a,b):
    return abs(a[0]-b[0])+abs(a[1]+b[1])

def iswall(p):
    n = p[0]**2 + 3*p[0] + 2 * p[0] * p[1] + p[1] + p[1]**2 + DESIGNERS_FAVORITE_NUMBER
    #print(n)
    #print(bin(n))
    return bin(n).count('1') % 2



def reconstruct_path(cameFrom, current):
    path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        path.append(current)
    
    path.reverse()
    return path


def A_star(start, goal, h):
    
    cameFrom = {}

    gScore = {}
    gScore[start] = 0

    fScore = {}
    fScore[start] = h(start)

    open_set = [Entry(fScore[start],start)]

    while len(open_set) != 0:
        
        current = heapq.heappop(open_set).coord
        
        if current == goal:
            # return the number of steps (gScore?)
            return (gScore[current],reconstruct_path(cameFrom, current))

            
        
        # for each neighbor
        for neighbor in [(current[0]-1,current[1]),(current[0]+1,current[1]),(current[0],current[1]-1),(current[0],current[1]+1)]:
            print(neighbor)
            if neighbor[0] < 0 or neighbor[1] < 0:
                continue
            if iswall(neighbor):
                continue
            tentative_gScore = gScore[current] + 1

            if neighbor not in gScore or tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor)

                if neighbor not in open_set:
                    heapq.heappush(open_set,Entry(fScore[neighbor],neighbor))


        print(open_set)
    
    return -1





print(A_star(start,goal,partial(taxicab,goal)))
