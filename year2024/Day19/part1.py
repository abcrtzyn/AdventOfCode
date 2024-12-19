# my input happens to have single string towels of all colors but green
# so...
# as long as I can find non-overlapping matches for all green striped things
# 


from typing import List, Dict
from functools import cache

# by prefix length (length of string before g)
towels_w_green: List[List[str]] = []

@cache
def pattern_possible(s: str) -> bool:
    # print(s)
    prefix_len = s.find('g')
    if prefix_len == -1:
        # no more greens to check
        return True

    test_cutoffs = set()

    for i in range(min(prefix_len,len(towels_w_green)-1),-1,-1):
        # for each prefix length
        for pattern in towels_w_green[i]:

            if s.startswith(pattern,prefix_len - i):
                cutoff = prefix_len-i + len(pattern)
                test_cutoffs.add(cutoff)
                
                # print(s)
                # print(' '*(prefix_len-i),pattern,sep='')
                # print(' '*cutoff,s[cutoff:],sep='')
    
    # for each test_cutoff, make sure the rest of the string is good, starting with the lowest cutoff
    # if it works with the lowest cutoff, it most likely works for larger ones too
    for cutoff in sorted(test_cutoffs):
        if pattern_possible(s[cutoff:]):
            # no need to check any further, awesome
            return True


    return False






with open('Day19/input.txt') as f:
    towels = [line.strip() for line in f.readline().split(',')]

    if not ('w' in towels and 'u' in towels and 'b' in towels and 'r' in towels):
        print('this program is only designed to handle inputs that have single stripe towels of all colors but green')
        print('sorry about that')
        exit(1)
    largest_towel = max(len(t) for t in towels)
    for _ in range(largest_towel):
        towels_w_green.append([])

    for towel in towels:
        prefix = towel.find('g')
        if prefix == -1:
            continue

        towels_w_green[prefix].append(towel)
        
    del towels

    f.readline()

    count = 0

    for line in f:
        result = pattern_possible(line.strip())
        count += result

    print('Part 1:',count)
