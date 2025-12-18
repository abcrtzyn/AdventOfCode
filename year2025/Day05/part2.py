

from typing import List, Tuple


ranges: List[Tuple[int,int]] = []


with open('Day05/input.txt','r') as f:
    for line in f:
        line = line.strip()
        if line == '':
            break
        numbers_strs = line.split('-')
        numbers = tuple([int(x) for x in numbers_strs])
        
        ranges.append(numbers) # type: ignore


fresh_numbers = 0

# this tracks current number that is being looked
current = 0

for r_low, r_high in sorted(ranges):
    if current < r_low:
        # There are no numbers between current and r_low that are fresh
        # count this full range
        fresh_numbers += (r_high - r_low + 1)
        # set current just past the range
        current = r_high + 1
    elif r_low <= current <= r_high:
        # [r_low,current) is already counted, count [current,r_high]
        fresh_numbers += (r_high - current + 1)
        # set current just past the range
        current = r_high + 1
    # elif r_high < current:
    #     # already counted every number in this range, no action
    #     pass

print(fresh_numbers)
