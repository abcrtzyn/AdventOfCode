from functools import partial
from hashlib import md5
from typing import Callable, Dict, Iterator, List, Tuple, cast

from python_utils.graph_traversals.shortest_path import a_star_parents

with open('Day17/input.txt') as f:
    key = f.read().strip()


# yet another time to implement a*

# implementating A* for this task


def add_direction(current: Tuple[int,int,str], direction: str):
    x = current[0] + ({'U':0,'D':0,'L':-1,'R':1}[direction])
    y = current[1] + ({'U':-1,'D':1,'L':0,'R':0}[direction])
    path = current[2] + direction
    return (x,y,path)


# taxicab distance, ignoring the path variable.
def taxicab(a: Tuple[int,int,str],b: Tuple[int,int,str]):
    return abs(a[0]-b[0])+abs(a[1]+b[1])


def get_neighbors(current: Tuple[int,int,str], current_score: int) -> Iterator[Tuple[int,Tuple[int,int,str]]]:
    hsh = md5(bytes(key+current[2],'utf-8')).hexdigest()[:4]

    directions = ['U','D','L','R']
    
    for d, c in zip(directions,hsh):
        next_node = add_direction(current,d)
        if not (1 <= next_node[0] <= 4 and 1 <= next_node[1] <= 4):
            continue
        if ord(c) < 98:
            continue

        yield 1,next_node


score, parents = a_star_parents(cast(Tuple[int,int,str],(1,1,'')),lambda x: x[0]==4 and x[1]==4,get_neighbors,partial(taxicab,(4,4,'')))

# we are not tracing parents to find the path, we are just stealing it from the node if we can find
for item in parents.keys():
    if item[0] == 4 and item[1] == 4:
        print('Part 1:',item[2])
        break



def max_path(start: Tuple[int,int,str], end: Callable[[Tuple[int,int,str]],bool]):
    """iterative depth first search. Runs to completion of the graph. Note the requirement that if you reach the end, that path stops there"""


    best_score = 0

    stack: List[Tuple[int,int,str]] = [start]
    scores: Dict[Tuple[int,int,str],int] = {start: 0}

    while stack:
        item = stack.pop()
        score = scores[item]

        if end(item):
            if score > best_score:
                best_score = score
            continue

        for edge_score, neighbor in get_neighbors(item,score):
            neighbor_score = score + edge_score

            if neighbor not in scores or neighbor_score > scores[neighbor]:
                scores[neighbor] = neighbor_score
                stack.append(neighbor)

    return best_score


print('Part 2:',max_path((1,1,''), lambda x: x[0] == 4 and x[1] == 4))

