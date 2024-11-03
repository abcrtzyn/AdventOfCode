
direction = 0

directions = {0:(1,0), 1:(0,1), 2:(-1,0), 3:(0,-1)}

# left is decrement
# right is increment

point = (0,0)

with open('Day01/input.txt') as f:
    line = f.readline()
    line = line.split(',')
    for x in line:
        a = x.strip()
        if a[0] == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        point = (point[0]+directions[direction][0]*int(a[1:]),point[1]+directions[direction][1]*int(a[1:]))
    print(abs(point[0])+abs(point[1]))
