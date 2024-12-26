
from itertools import combinations
from typing import Dict, List, Set


network: Dict[str,List[str]] = {}

# make the network
with open('Day23/input.txt') as f:
    for line in f:
        a,b = line.strip().split('-')

        if a not in network:
            network[a] = []
        network[a].append(b)
        if b not in network:
            network[b] = []
        network[b].append(a)


groups3: Set[str] = set()

# for each node that begins with t
for node in network:
    if node[0] != 't':
        continue

    for node2, node3 in combinations(network[node],2):
        # if node2 and node3 are connected, its good
        if node3 in network[node2]:
            groups3.add(''.join(sorted([node,node2,node3])))

print('Part 1:',len(groups3))
