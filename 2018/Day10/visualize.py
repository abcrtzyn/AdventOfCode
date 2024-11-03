ITERATIONS = 10710

import numpy as np
import re

line_rule = re.compile("position=<([ -]\\d+), ([ -]\\d+)> velocity=<([ -]\\d+), ([ -]\\d+)>")


points = []

with open('Day10/input.txt') as f:
    for line in f:
        mat = line_rule.match(line)
        if mat == None:
            exit(1)
        
        px,py,vx,vy = [int(x) for x in mat.groups()]

        points.append((px+ITERATIONS*vx,py+ITERATIONS*vy,vx,vy))


# get the size of the grid
# min_x = 10000000
# max_x = -10000000
# min_y = 10000000
# max_y = -10000000

# for i in range(len(points)):
#     px,py,vx,vy = points[i]
#     if px < min_x:
#         min_x = px
#     elif px > max_x:
#         max_x = px
#     if py < min_y:
#         min_y = py
#     elif py > max_y:
#         max_y = py

# print(max_x-min_x,max_y-min_y)
import matplotlib.pyplot as plt

#  it will be much easier to make a scatter plot
xs = [p[0] for p in points]
ys = [-p[1] for p in points]

plt.scatter(xs,ys)
plt.show()
