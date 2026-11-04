

from collections import defaultdict
from typing import Dict, List, Tuple

import numpy as np


with open('Day23/input.txt') as f:
    grid = np.array([[y for y in x.strip()] for x in f.readlines()])

counts = np.zeros(grid.shape)

#print(grid)

start = (0,1)
end = (grid.shape[0]-1,grid.shape[1]-2)
UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)
directions: List[Tuple[int,int]] = [UP,DOWN,LEFT,RIGHT]
opposite: Dict[Tuple[int,int],Tuple[int,int]] = {UP:DOWN,DOWN:UP,LEFT:RIGHT,RIGHT:LEFT}

queue: List[Tuple[Tuple[int,int],Tuple[int,int]]] = [(start,DOWN)]

# we could count all the paths seperately
paths: List[Tuple[Tuple[int,int],Tuple[int,int],int]] = []

def tile_add(tile1: Tuple[int,int],tile2: Tuple[int,int]):
    return (tile1[0]+tile2[0],tile1[1]+tile2[1])

def isjunction(tile: Tuple[int,int]):
    paths = 0
    for dire in directions:
        paths += grid[tile_add(tile,dire)] != '#'
    return paths >= 3

while len(queue) != 0:
    tileo,dire = queue.pop(0)
    tile = tileo

    # keep moving until we hit a junction or end
    tile = tile_add(tile,dire)
    step_count = 1

    while (tile != end and not isjunction(tile)):
        # move to the next tile
        new_tile = (0,0)
        new_dire = (0,0)
        for dire2 in directions:
            #print(dire,dire2)
            if dire2 != opposite[dire]:
                #print('not opposite')
                if grid[tile[0]+dire2[0],tile[1]+dire2[1]] != '#':
                    new_tile = tile_add(tile,dire2)
                    new_dire = dire2
                    #print('new',new_tile)
        tile = new_tile
        dire = new_dire
        step_count += 1
    
    # this brings us to a junction
    #print(step_count)

    # if tile,tileo is already in paths, no need to put offshoots in the queue (they have already been done)
    if (tileo,tile) in [(x[0],x[1])for x in paths]:
        continue
    paths.append((tileo,tile,step_count))
    paths.append((tile,tileo,step_count))
    if tile == end:
        continue
    # for each direction of tile not opposite of dire, add to queue
    for dire2 in directions:
        #print(dire,dire2)
        if dire2 != opposite[dire]:
            #print('not opposite')
            if grid[tile[0]+dire2[0],tile[1]+dire2[1]] != '#':
                queue.append((tile,dire2))
    #print(queue)

adj: Dict[Tuple[int,int],List[Tuple[Tuple[int,int],int]]] = defaultdict(list)
for x,y,c in paths:
    adj[x].append((y,c))
#print(adj)
# this is essientially an adjacency matrix
nodes_n = len(adj.keys())

# this stuff should be enough to find a maximal route
# find the longest path from start to end by trying everything
def find_path(x: Tuple[int,int],y: Tuple[int,int],visited: Dict[Tuple[int,int],int]) -> int:
    #print('cur',x,visited)
    if x == y:
        return 0
    visited[x] = 1
    mp = 0
    for n,c in adj[x]:
        if not visited[n]:
            mp = max(mp,c+find_path(n,y,visited))
    visited[x] = 0
    
    return mp

visited = {x:0 for x in adj.keys()}

print(find_path(start,end,visited))



