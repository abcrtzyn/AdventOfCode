import re
from typing import List

towerHeight = 8
towerN = 9



with open('Day05/input.txt') as f:
    h: List[str] = list()
    for i in range(towerHeight):
        h.append(f.readline())
    
    h.reverse()

    stacks: List[List[str]] = list()
    
    for t in range(towerN):
        a = list()
        for line in h: 
            c = line[t*4+1]
            if(c == ' '): break
            a.append(line[t*4+1])
        stacks.append(a)
    
    f.readline()
    f.readline()

    exp = re.compile('move (\d+) from (\d+) to (\d+)')
    for line in f:
        m = exp.match(line)
        n = int(m.group(1))
        p = int(m.group(2))-1
        q = int(m.group(3))-1
        
        stacks[q].extend(stacks[p][-n:])
        stacks[p] = stacks[p][:-n]
        
    for a in stacks:
        print(a[-1],end='')