from operator import add
from typing import List
import itertools

target = 150

containers: List[int] = []

with open('Day17/input.txt') as f:
    for line in f.readlines():
        containers.append(int(line.strip()))



min_acc_sums = itertools.accumulate(sorted(containers),add)
max_combo_length = next((i for i, v in enumerate(min_acc_sums) if v > target), -1)

max_acc_sums = itertools.accumulate(reversed(sorted(containers)),add)
min_combo_length = next((i for i, v in enumerate(max_acc_sums) if v > target), -1)+1
# note that this value is a guess. There could still be zero ways depending on the actual values


ways = 0
# trying all possible combinations of all lengths, maybe not the last one
# this is not efficient because there are ways to ignore various branches of the combinations trees
minimum_length_combinations = 0

for i in range(min_combo_length,max_combo_length+1):
    # isn't this just significantly smaller than the previous version I had
    pways = sum((150-sum(com)==0) for com in itertools.combinations(containers,i))
    if pways > 0 and minimum_length_combinations == 0:
        minimum_length_combinations = pways
    
    ways += pways

        
print('Part 1:',ways)

print('Part 2:',minimum_length_combinations)
