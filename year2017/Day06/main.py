
from typing import Dict, List, Tuple


current: List[int] = []

with open('Day06/input.txt') as f:
    current = [int(x) for x in f.read().split()]

length = len(current)

states: Dict[Tuple[int,...],int] = {}

iterations = 0

while True:
    # get the index with the most blocks
    i = current.index(max(current))
    # remove all blocks from i and redistribute
    v = current[i]
    current[i] = 0
    
    # there is a better way to do this
    # for each block
    for j in range(1,v+1):
        # add it to the index
        current[(i+j)%length] += 1
    
    iterations += 1

    if tuple(current) in states:
        # we've seen this before, done
        break
    
    states[tuple(current)] = iterations


print('Part 1:',iterations)
print('Part 2:',iterations-states[tuple(current)])
exit(0)
