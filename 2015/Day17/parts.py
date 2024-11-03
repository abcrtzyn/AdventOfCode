containers = []

with open('Day17/input.txt') as f:
    for line in f.readlines():
        containers.append(int(line.strip()))

print(containers)

import itertools

ways = 0
# trying all possible combinations
for i in range(len(containers)):
    for com in itertools.combinations(containers,i):
        liquid = 150
        for c in com:
            liquid -= c
            if liquid < 0:
                break
        if liquid == 0:
            ways += 1
    

print(ways)

ways = 0

for com in itertools.combinations(containers,4):
    liquid = 150
    for c in com:
        liquid -= c
        if liquid < 0:
            break
    if liquid == 0:
        ways += 1

print(ways)


