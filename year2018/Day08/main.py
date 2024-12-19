
from typing import List





# lets first see if the second part requires full parsing

def sum_meta(l: List[int]) -> int:
    total = 0

    child = l.pop(0)
    meta = l.pop(0)

    for _ in range(child):
        total += sum_meta(l)
    
    for _ in range(meta):
        total += l.pop(0)
    
    return total

def value(l: List[int]) -> int:
    node_value = 0

    child = l.pop(0)
    meta = l.pop(0)

    child_values = []

    if child == 0:
        # value is sum_meta
        for _ in range(meta):
            node_value += l.pop(0)
    else:
        # value is based on child values
        for _ in range(child):
            child_values.append(value(l))
        
        for _ in range(meta):
            n = l.pop(0)
            if n <= child:
                node_value += child_values[n-1]
    
    return node_value


with open('Day08/input.txt') as f:
    the_list = [int(x) for x in f.read().split(' ')]
    print(sum_meta(the_list.copy()))
    print(value(the_list))
