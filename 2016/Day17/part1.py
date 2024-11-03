from hashlib import md5

key = 'veumntbg'


# yet another time to implement a*

# implementating A* for this task

from functools import partial
import heapq
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Entry:
    priority: int
    path: Any=field(compare=False)


goal = (4,4)

def get_coord(path):
    x = 1
    y = 1
    for c in path:
        match c:
            case 'U': y -= 1
            case 'D': y += 1
            case 'L': x -= 1
            case 'R': x += 1
            case _:
                print('not a direction character')
                exit(1)
    return (x,y)

# taxicab distance
def taxicab(a,b):
    return abs(a[0]-b[0])+abs(a[1]+b[1])



def A_star(goal):

    gScore = {}
    gScore[''] = 0

    fScore = {}
    fScore[''] = taxicab((1,1),goal)

    open_set = [Entry(fScore[''],'')]

    while len(open_set) != 0:
        
        current = heapq.heappop(open_set).path
        current_coord = get_coord(current)



        if current_coord == goal:
            return current

            
        
        # for each neighbor

        hsh = md5(bytes(key+current,'utf-8')).hexdigest()[:4]


        for npath,ncoord,nch in zip([current+'U',current+'D',current+'L',current+'R'],
                            [(current_coord[0],current_coord[1]-1),(current_coord[0],current_coord[1]+1),(current_coord[0]-1,current_coord[1]),(current_coord[0]+1,current_coord[1])],
                            hsh):
            #print(npath,ncoord,nch)
            
            if ncoord[0] < 1 or ncoord[1] < 1:
                continue
            if ord(nch) < 98:
                continue

            tentative_gScore = gScore[current] + 1
            gScore[npath] = tentative_gScore
            fScore[npath] = tentative_gScore + taxicab(ncoord,goal)
            
            heapq.heappush(open_set,Entry(fScore[npath],npath))

        print(open_set)
    
    return -1






print(A_star(goal))
