
from heapq import heapify, heappop, heappush
from typing import Dict, List, Union

def work_time(letter: str):
    return ord(letter) - 4


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

current_time = 0

done_time = [0,0,0,0,0]
projects: List[Union[str,None]] = [None,None,None,None,None]

while True:
    # print(queue)
    # print(projects)
    # print(done_time)
    
    # if there is an elf and project available, start a project
    if None in projects and queue:
        # grab the next element
        i = projects.index(None)
        e = heappop(queue)
        projects[i] = e
        done_time[i] = current_time + work_time(e)
    else: # no workers or projects available
        # increase the current time
        minimum = min(done_time)
        if minimum == 1000000000:
            break
        current_time = minimum
        while current_time in done_time: # make sure to grab all workers that are finished at the same time
            i = done_time.index(current_time)
            e = projects[i]
            projects[i] = None
            done_time[i] = 1000000000

            # when the project is done, adjust the requirements
            if e in outgoing:
                for next_node in outgoing[e]:
                    # remove the requirement from incoming nodes
                    incoming[next_node].remove(e)
                    if len(incoming[next_node]) == 0:
                        # all requirements fulfilled
                        heappush(queue,next_node)


print(current_time)
