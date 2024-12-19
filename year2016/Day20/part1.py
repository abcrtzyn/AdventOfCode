# I think sorting the rules is going to be a good idea
# starting with 0, if there is a rule that blocks 0, try the next ip above that rule

# some part of this reminds me of interval search

# 0 - 9000

# if there is a rule that starts below 9000 and has a greater limit,
#   look at that endpoint

import re
import bisect

line_format = re.compile('(\\d+)-(\\d+)')


rules = []


with open('Day20/input.txt') as f:
    for line in f.readlines():
        mat = line_format.match(line)
        if mat is None:
            print(f'"{line}" not parsed')
            exit(1)
        start = int(mat.group(1))
        end = int(mat.group(2))
        
        rules.insert(bisect.bisect(rules,(start,end)),(start,end))
        

allowed = []
allowed_count = 0

current = 0

for rulelo,rulehi in rules:
    if current > rulehi:
        continue
    elif current < rulelo:
        allowed.append((current,rulelo-1))
        allowed_count += rulelo - current
        current = rulehi + 1
    elif rulelo <= current <= rulehi:
        current = rulehi + 1


# print(allowed)
print(allowed_count)
