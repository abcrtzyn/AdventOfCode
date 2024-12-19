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

grid = np.zeros((x_max-x_min+20,y_max-y_min+20),np.int8)

# when marking, grid_index + (xy)_min - 10 = coordinate position

def dist(cx,cy,px,py):
    return abs(cx-px) + abs(cy-py)


# ill try make an array version later, for now, a loop
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        min_d_point = 0
        min_d = 10000
        for pi,p in enumerate(points):
            d = dist(i+x_min-10,j+y_min-10,p[0],p[1])
            # print(d)
            if d < min_d:
                min_d = d
                min_d_point = pi
        # print(i,j,min_d_point)
        grid[i,j] = min_d_point
        # exit(0)

# print(grid)
# exit(0)

largest_area = 0
largest_area_point = 0
for x,p in enumerate(points):
    marks = grid==x
    area = np.count_nonzero(marks)
    if area > largest_area:
        # check that there are no marks at the edge
            if not (np.count_nonzero(marks[0,:]) or np.count_nonzero(marks[:,0]) or np.count_nonzero(marks[-1,:]) or np.count_nonzero(marks[:,-1])):
                largest_area = area
                largest_area_point = x

print(largest_area_point,largest_area)
