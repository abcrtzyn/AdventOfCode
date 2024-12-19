
import numpy as np
import re


# grid_shape = (11,7)
grid_shape = (101,103)


line_rule = re.compile('p=(\\d+),(\\d+) v=(-?\\d+),(-?\\d+)')


entities_positions = []
entities_velocities = []


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
        
        entities_positions.append((px,py))
        entities_velocities.append((vx,vy))

np.set_printoptions(threshold=100000,linewidth=10000)

# im going to guess that its not going to have any duplicates on any cells
# i was right, no garentees for other inputs

i = 0
while True:
    i += 1

    grid = np.zeros(grid_shape,np.uint16)
    # simulate
    flag = True

    for j in range(len(entities_positions)):
        px,py = entities_positions[j]
        vx,vy = entities_velocities[j]
        px = (px + vx) % grid_shape[0]
        py = (py + vy) % grid_shape[1]
        entities_positions[j] = (px,py)

        if grid[px,py] != 0:
            flag = False
        grid[px,py] += 1
    
    if flag:
        print(grid)
        print('I can not garuntee that this answer is correct for every input')
        print('Part 2:',i)
        exit(0)
