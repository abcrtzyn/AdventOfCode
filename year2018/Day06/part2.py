import numpy as np

points = []


# parse
with open('Day06/input.txt') as f:
    for line in f:
        points.append(tuple(int(x) for x in line.strip().split(', ')))


x_min = 200
x_max = 200
y_min = 200
y_max = 200
# get min and max
for px,py in points:
    if px > x_max:
        x_max = px
    elif px < x_min:
        x_min = px
    if py > y_max:
        y_max = py
    elif py < y_min:
        y_min = py

grid = np.zeros((x_max-x_min+20,y_max-y_min+20),np.int16)

# when marking, grid_index + (xy)_min - 10 = coordinate position

def dist(cx,cy,px,py):
    return abs(cx-px) + abs(cy-py)


# ill try make an array version later, for now, a loop
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        grid[i][j] = sum([dist(i+x_min-10,j+y_min-10,px,py) for px,py in points])

print(np.count_nonzero(grid < 10000))
