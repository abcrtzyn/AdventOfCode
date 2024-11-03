
direction = 0

directions = {0:(1,0), 1:(0,1), 2:(-1,0), 3:(0,-1)}

# left is decrement
# right is increment

locations = set()

point = (0,0)
locations.add(point)

with open('Day01/input.txt') as f:
    line = f.readline()
    line = line.split(',')
    for x in line:
        a = x.strip()
        if a[0] == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        dp = directions[direction]
        for i in range(int(a[1:])):
            print(point)
            point = (point[0] + dp[0],point[1] + dp[1])
            if point in locations:
                # done
                print(point)
                print(abs(point[0])+abs(point[1]))
                exit()
            else:
                locations.add(point)
