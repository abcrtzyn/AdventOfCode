# Find the largest clique in the graph
# I've never had to solve this problem
# I have looked up the Bron–Kerbosch algorithms

from typing import Dict, List, Set


network: Dict[str,Set[str]] = {}

# make the network
with open('Day23/input.txt') as f:
    for line in f:
        a,b = line.strip().split('-')

        if a not in network:
            network[a] = set()
        network[a].add(b)
        if b not in network:
            network[b] = set()
        network[b].add(a)



# Bron–Kerbosch algorithm, first version. plenty fast enough for this number of nodes
def find_largest_clique(check: Set[str]):
    if len(check) == 1:
        return check

    largest_size = -1
    largest_clique: Set[str] = set()
    # pick a node in check, likely the one with the most neighbors
    not_checked = check.copy()

    for node in check:
        # by precondition, it is connected to all nodes in required
        nextcheck = network[node].intersection(not_checked)
        result = find_largest_clique(nextcheck)
        if len(result) > largest_size:
            largest_size = len(result)
            largest_clique = result
            largest_clique.add(node)
        
        not_checked.remove(node)
    
    return largest_clique
    


clique = find_largest_clique(set(network.keys()))


print('Part 2:', ','.join(sorted(list(clique))))
