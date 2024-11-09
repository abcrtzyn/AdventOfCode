from typing import List


containers = []

with open('Day17/input.txt') as f:
    for line in f.readlines():
        containers.append(int(line.strip()))

# print(containers)


# Now for a more efficient solution using backtracking, tree traversal

def fill(containers: List[int], next_container: int, amount: int) -> int:
    # starting at the next container
    # try using the rest of the containers
    ways = 0
    for i in range(next_container,len(containers)):
        working_amount = amount - containers[i]
        if working_amount == 0:
            ways += 1
        elif working_amount > 0:
            # still fluid left, try add another container
            ways += fill(containers, i+1, working_amount)
        # else working_about < 0, underflow do nothing
    
    return ways

print('Part 1:',fill(containers, 0, 150))


import itertools
# there are ways I could sneakily incorporate part 2 into part 1, but I'm not going to

for i in range(len(containers)):
    ways = sum((150-sum(com)==0) for com in itertools.combinations(containers,i))
    if ways > 0:
        break
        
print('Part 2:',ways)
