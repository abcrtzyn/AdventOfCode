# m = 0
# m1 = 0
# n = 0
# n1 = 0
# acc = 0
# acc1 = 0
# with open('Day18/input.txt') as f:
#     for line in f.readlines():
#         x = line.split(' ')
#         if x[0] == 'U':
#             acc += int(x[1])
#             m = max(m,acc)
#             m1 = min(m1,acc)
#         if x[0] == 'D':
#             acc -= int(x[1])
#             m = max(m,acc)
#             m1 = min(m1,acc)
#         if x[0] == 'R':
#             acc1 += int(x[1])
#             n = max(n,acc1)
#             n1 = min(n1,acc1)
#         if x[0] == 'L':
#             acc1 -= int(x[1])
#             n = max(n,acc1)
#             n1 = min(n1,acc1)
# print(acc, m, m1)
# print(acc1,n, n1)

# max size for this input, -86, 290 UD, -179, 391 LR
import numpy as np

grid = np.zeros((291+87+2,391+180+2),np.bool8)
# grid = np.zeros((11,11),np.uint8)
x = 180
y = 87
grid[y,x] = True

with open('Day18/input.txt') as f:
    for line in f.readlines():
        line2 = line.split(' ')
        if line2[0] == 'U':
            for i in range(int(line2[1])):
                y -= 1
                grid[y,x] = True
        elif line2[0] == 'D':
            for i in range(int(line2[1])):
                y += 1
                grid[y,x] = True
        elif line2[0] == 'L':
            for i in range(int(line2[1])):
                x -= 1
                grid[y,x] = True
        elif line2[0] == 'R':
            for i in range(int(line2[1])):
                x += 1
                grid[y,x] = True

# intermediate check to make sure the correct number of steps were made
#print(grid)

print('hi')
# when going through a row, 
# if the cell is the first edge
    # count it
    # turn on edge flag
    # if the cell above is true, mark up as true
# if the cell is not an edge
    # if the edge flag is on, turn it off and 
        # if up is on and the cell down and left is True, flip inside flag
    # if the inside flag is on, count the cell


edge = False
multiedge = False
up = False
inside = False

acc = 0
for i, row in enumerate(grid):
    #print(row)
    #acc = 0
    edge = False
    multiedge = False
    inside = False
    for j,cell in enumerate(row):
        if cell == True:
            if edge:
                multiedge = True;
            else:
                edge = True
                up = grid[i-1,j]
            acc += 1
        else:
            if edge:
                if multiedge:
                    if up != grid[i-1,j-1]:
                        inside = not inside
                else:
                    inside = not inside
                
                edge = False
                multiedge = False
                
            if inside:
                acc += 1
        #print('edge', edge, 'multi', multiedge, 'up', up, 'inside', inside)
    #print(acc)

print(acc)