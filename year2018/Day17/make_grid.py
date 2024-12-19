
# all of the first coordinates are single coordinates
# the second ones are slices

import re

rule = re.compile('(x|y)=(\\d+), (x|y)=(\\d+)\\.\\.(\\d+)')


parsed = []

min_x = 500
max_x = 500
max_y = 0

with open('Day17/input.txt') as f:
    for line in f:
        mat = rule.match(line)
        if mat is None:
            print('could not parse something')
            exit(1)
        inline = mat.group(1)
        first = int(mat.group(2))
        second = int(mat.group(4))
        third = int(mat.group(5))
        if mat.group(3) == inline:
            print('same coordinate? no way')
            exit(1)
        parsed.append((inline,first,second,third))

        # figure maxs and min
        if inline == 'x':
            if first < min_x:
                min_x = first
            elif first > max_x:
                max_x = first
            if third > max_y:
                max_y = third
        else:
            if first > max_y:
                max_y = first
            if second < min_x:
                min_x = second
            if third > max_x:
                max_x = third

print(min_x)
print(max_x)
print(max_y)

import numpy as np

grid = np.zeros((max_y+1,(max_x-min_x+1)),dtype=np.uint8)
# grid.fill(ord('.'))


grid[0,500-min_x] = 2 #ord('+')

for d,f,s,t in parsed:
    if d == 'x':
        grid[s:t+1,f-min_x] = 1 #ord('#')
    if d == 'y':
        grid[f,(s-min_x):(t-min_x+1)] = 1 #ord('#')

np.savetxt('Day17/grid.txt',grid,'%u',' ')
# np.savetxt('Day17/grid.txt',grid,'%c','')
