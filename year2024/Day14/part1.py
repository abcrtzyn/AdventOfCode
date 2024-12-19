
from functools import reduce
import re

# grid_shape = (11,7)
grid_shape = (101,103)

quad_x_boundries = ((0,grid_shape[0]//2),(grid_shape[0]//2+1,grid_shape[0]))
quad_y_boundries = ((0,grid_shape[1]//2),(grid_shape[1]//2+1,grid_shape[1]))


line_rule = re.compile('p=(\\d+),(\\d+) v=(-?\\d+),(-?\\d+)')

quad_count = [0] * 4

with open('Day14/input.txt') as f:
    for line in f:
        mat = line_rule.match(line)

        if mat is None:
            print('could not parse',line)
            exit(1)
        px = int(mat.group(1))
        py = int(mat.group(2))
        vx = int(mat.group(3))
        vy = int(mat.group(4))
        
        # add 100 seconds of time
        px += vx * 100
        px %= grid_shape[0]

        py += vy * 100
        py %= grid_shape[1]

        left = False
        right = False
        up = False
        down = False


        if quad_x_boundries[0][0] <= px < quad_x_boundries[0][1]:
            left = True
        elif quad_x_boundries[1][0] <= px < quad_x_boundries[1][1]:
            right = True
        
        if quad_y_boundries[0][0] <= py < quad_y_boundries[0][1]:
            up = True
        elif quad_y_boundries[1][0] <= py < quad_y_boundries[1][1]:
            down = True

        if left and up:
            quad_count[0] += 1
        elif left and down:
            quad_count[1] += 1
        elif right and up:
            quad_count[2] += 1
        elif right and down:
            quad_count[3] += 1



print('Part 1:', reduce(lambda x, y: x*y, quad_count))
        
