
from heapq import heapify, heappop, heappush
from typing import Dict, List


# I can confirm all letters exist

queue = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

outgoing: Dict[str,List[str]] = {}
incoming: Dict[str,List[str]] = {}



with open('Day07/input.txt') as f:
    for line in f:
        start = line[5]
        end = line[36]
        if end in queue:
            queue.remove(end)
        
        if start in outgoing:
            outgoing[start].append(end)
        else:
            outgoing[start] = [end]
        
        if end in incoming:
            incoming[end].append(start)
        else:
            incoming[end] = [start]


queue = list(queue)
heapify(queue)

order = ''

while queue: # has length
    # grab the next element
    e = heappop(queue)
    order += e
    if e in outgoing:
        for next_node in outgoing[e]:
            # remove the requirement from incoming nodes
            incoming[next_node].remove(e)
            if len(incoming[next_node]) == 0:
                # all requirements fulfilled
                heappush(queue,next_node)


print(order)
