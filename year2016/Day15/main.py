import re
from typing import List, Tuple

line_re = re.compile('Disc #\\d+ has (\\d+) positions; at time=0, it is at position (\\d+)\\.')

# mod value, position
discs: List[Tuple[int,int]] = []

with open('Day15/input.txt','r') as f:
    for disc, line in enumerate(f):
        mat = line_re.match(line)
        if mat == None:
            print('could not match the line')
            print(line)
            exit(1)
        mod = int(mat.group(1))
        pos = int(mat.group(2))
        # time offset position
        pos = (pos+disc+1) % mod

        discs.append((mod,pos))

print(discs)

# I believe I have to, for each disc
# find the first x where (pos + x) % mod = 0 above the previous with some other limitations

def solve(discs: List[Tuple[int,int]]):
    mult = 1
    x = 0
    for mod, pos in discs:
        # add on the multiplier until the desired mod is reached
        while (x+pos) % mod != 0:
            x += mult
        
        # add that discs frequency to the multiplier
        mult *= mod
    
    return x



print('Part 1: ', solve(discs))

# add the next disc. It will be reached at t=7, so add 7 to the position.
# I actually don't know how many discs are in the input so len+1 will be the correct value regardless
discs.append((11,0+1+len(discs)))

print('Part 2: ', solve(discs))
