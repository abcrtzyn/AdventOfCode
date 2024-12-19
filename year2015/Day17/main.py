containers = []

with open('Day17/input.txt') as f:
    for line in f.readlines():
        containers.append(int(line.strip()))

# print(containers)

import itertools

ways = 0
# trying all possible combinations of all lengths, maybe not the last one
# this is not efficient because there are ways to ignore various branches of the combinations trees
for i in range(len(containers)):
    # isn't this just significantly smaller than the previous version I had
    ways += sum((150-sum(com)==0) for com in itertools.combinations(containers,i))
        
print('Part 1:',ways)



                                                                         # 4 is the minimum containers in my case
ways  = sum((150-sum(com)==0) for com in itertools.combinations(containers,4))
    
print('Part 2:',ways)
