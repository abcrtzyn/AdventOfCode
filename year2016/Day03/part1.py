count = 0
with open('Day03/input.txt') as f:
    i = 0
    for line in f.readlines():
        line = [int(x) for x in line.strip().split()]
        if (line[0]-line[1]-line[2] < 0) and (line[1]-line[2]-line[0] < 0) and (line[2]-line[0]-line[1] < 0):
             # possible triangles
             count += 1


print('Part 1:', count)