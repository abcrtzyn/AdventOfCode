import re
from typing import List

towerHeight = 8
towerN = 9



with open('Day05/input.txt') as f:
    h: List[str] = []
    for i in range(towerHeight):
        h.append(f.readline())
    
    h.reverse()

    stacks: List[List[str]] = []
    
    for t in range(towerN):
        a: List[str] = []
        for line in h: 
            c = line[t*4+1]
            if(c == ' '): break
            a.append(line[t*4+1])
        stacks.append(a)
    
    f.readline()
    f.readline()

    exp = re.compile('move (\\d+) from (\\d+) to (\\d+)')
    for line in f:
        m = exp.match(line)
        if m is None:
            print('could not match line')
            exit(1)
        n = int(m.group(1))
        p = int(m.group(2))-1
        q = int(m.group(3))-1
        for _ in range(n):
            stacks[q].append(stacks[p].pop())
    
    for a in stacks:
        print(a[-1],end='')
