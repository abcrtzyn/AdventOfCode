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



def distinct(start, steps):
    
    cameFrom = {}

    gScore = {}
    gScore[start] = 0

    open_set = [Entry(gScore[start],start)]

    while len(open_set) != 0:
        
        current = heapq.heappop(open_set).coord

        if gScore[current] > steps:
            # done
            print(gScore)
            count = 0
            for k,v in gScore.items():
                if v <= steps:
                    count += 1
            
            return count

        # for each neighbor or current
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

                if neighbor not in open_set:
                    heapq.heappush(open_set,Entry(gScore[neighbor],neighbor))


        print(open_set)
    
    return -1





print(distinct(start,50))
