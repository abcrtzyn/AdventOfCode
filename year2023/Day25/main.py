# we are told there are three edges that if removed will split the graph into two parts
# the goal is to find them

# it is not easy to determine if a graph is connected (every vertex to every vertex)
# i think 1224 nodes will be perfectly okay for flourish to handle
from typing import List,Dict


verts: Dict[str,List[str]] = {}

with open('Day25/input.txt') as f:
    for line in f.readlines():
        v, line = line.split(':')
        dests = line.strip().split(' ')
        for x in dests:
            if v not in verts:
                verts[v] = []
            if x not in verts:
                verts[x] = []
            
            verts[v].append(x)
            verts[x].append(v)

# my edges are kcn,szl   ptq,fxn    lzd,fbd

verts['kcn'].remove('szl')
verts['szl'].remove('kcn')
verts['ptq'].remove('fxn')
verts['fxn'].remove('ptq')
verts['lzd'].remove('fbd')
verts['fbd'].remove('lzd')

# count the number of verticies
visited = {k: False for k in verts.keys()}

queue = ['szl']
visited['szl'] = True

while len(queue) > 0:
    current = queue.pop(0)

    for a in verts[current]:
        if visited[a] == False:
            visited[a] = True
            queue.append(a)

c = 0
for i in visited:
    if visited[i]:
        c += 1

print(c)