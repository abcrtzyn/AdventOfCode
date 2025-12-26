

from typing import Dict, List, Set, Tuple


connections: Dict[str,List[str]] = {}
# paths will store the number of paths that contain fft, dac, both, or none
paths: Dict[str,Tuple[int,int,int,int]] = {}
visitied: Set[str] = set()

with open('Day11/input.txt','r') as f:

    for line in f:
        nmenos = line.split()
        connections[nmenos[0][:-1]] = nmenos[1:]


def count_paths(node: str) -> Tuple[int,int,int,int]:
    if node in paths:
        return paths[node]
    
    # if the node is not in paths but is visited, there is a loop and we need to stop
    if node in visitied:
        # loop of some sort
        print('there are loops')
        print(visitied)
        print(node)
        print(paths)
        exit(1)
    
    visitied.add(node)

    acc_none = 0
    acc_dac = 0
    acc_fft = 0
    acc_both = 0

    for branch in connections[node]:
        res_none, res_dac, res_fft, res_both = count_paths(branch)
        acc_none += res_none
        acc_dac += res_dac
        acc_fft += res_fft
        acc_both += res_both
    
    if node == 'fft':
        acc_fft += acc_none
        acc_none = 0
        acc_both += acc_dac
        acc_dac = 0
    elif node == 'dac':
        acc_dac += acc_none
        acc_none = 0
        acc_both += acc_fft
        acc_fft = 0


    paths[node] = (acc_none,acc_dac,acc_fft,acc_both)
    return (acc_none,acc_dac,acc_fft,acc_both)

paths['out'] = (1,0,0,0)

print('Part 1:',sum(count_paths('you')))

print('Part 2:',count_paths('svr')[3])

