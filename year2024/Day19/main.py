from typing import Dict, List
from functools import cache

# counts the number of ways to make each towel arrangement
# {first char: [strings sorted by length reversed]}
towels: Dict[str,List[str]] = {}

# it is likely that this function call will see lots of the same starting position
# the cache decorator means that it will store results and use them rather than re-computing each time
@cache
def count_possibles(s: str, starting: int = 0) -> int:
    # print(s)
    if starting == len(s):
        return 1
    
    count = 0
    if s[starting] not in towels:
        return 0
    
    for pattern in towels[s[starting]]:
        if s.startswith(pattern,starting):
            count += count_possibles(s,starting+len(pattern))

    return count


with open('Day19/input.txt') as f:
    towel_strings = [line.strip() for line in f.readline().split(',')]

    for towel in towel_strings:
        if towel[0] not in towels:
            towels[towel[0]] = []
        towels[towel[0]].append(towel)
    
    # reverse sort each in towels, longest to shortest. It likely doesn't effect speed but I like to think it will
    for k in towels:
        towels[k] = sorted(towels[k],reverse=True)
    
    # read the empty line
    f.readline()

    count_strings = 0
    count_ways = 0

    for line in f:
        # how many ways to assemble the string
        result = count_possibles(line.strip())
        if result > 0:
            count_strings += 1
        count_ways += result

    print('Part 1:',count_strings)
    print('Part 2:',count_ways)
