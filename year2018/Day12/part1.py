# parse the rules
# create a lookup for ints (0,0,0,0,0) -> 0

import re
rule_rule = re.compile('([#.]{5}) => ([#.])')


rules = {}





with open('Day12/input.txt') as f:
    initial = [1 if c=='#' else 0 for c in f.readline().strip()[15:]]
    f.readline()
    for line in f:
        # parse a rule
        mat = rule_rule.match(line)
        if mat is None:
            exit(1)
        s = [c=='#' for c in mat.group(1)]
        n = s[0] + 2*s[1] + 4*s[2] + 8*s[3] + 16*s[4]
        r = 1 if mat.group(2) == '#' else 0

        rules[n] = r


# print(rules)


# have a list of elements that can grow in both directions

ITERATIONS = 500

# keep track of zero
state = [0]*10 + initial + [0]*(ITERATIONS+2)
zero = 10


for j in range(ITERATIONS):
    # print(''.join(['#' if x else '.' for x in state]))
    newstate = [0]*len(state)
    for i in range(2,len(state)-2):
        # look at cells two on either side
        key = state[i-2] + 2*state[i-1] + 4*state[i] + 8*state[i+1] + 16*state[i+2] 
        newstate[i] = rules[key]

    state = newstate

    score = 0
    for i,x in enumerate(state,-zero):
        score += i*x

    print(j+1,',',score)


# print(''.join(['#' if x else '.' for x in state]))
