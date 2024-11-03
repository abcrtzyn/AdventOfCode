# rule parsing

import re

bot_rule = re.compile('bot (\\d+) gives low to (bot|output) (\\d+) and high to (bot|output) (\\d+)')
value_rule = re.compile('value (\\d+) goes to bot (\\d+)')

rules = {}
values = []

with open('Day10/input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        
        bot_match = bot_rule.match(line)
        if bot_match is not None:
            rules[int(bot_match.group(1))] = (int(bot_match.group(3))+(300 if bot_match.group(2) == 'output' else 0), int(bot_match.group(5)) + (300 if bot_match.group(4) == 'output' else 0))
            continue
        value_match = value_rule.match(line)
        if value_match is not None:
            values.append((int(value_match.group(2)),int(value_match.group(1))))

# now create bot states stuff
bots = {}

process_stack = []

# initial states
for k,v in values:
    if k in bots:
        bots[k].append(v)
        if len(bots[k]) >= 2:
            process_stack.append(k)
    else:
        bots[k] = [v]

while len(process_stack) != 0:
    #print(process_stack)
    p = process_stack.pop()

    e1 = bots[p].pop(0)
    e2 = bots[p].pop(0)
    if len(bots[p]) >= 2:
        process_stack.append(p)
    """Part 1 check"""
    if (e1==61 and e2==17) or (e1==17 and e2==61):
        print(f'bot {p} is handling 61 and 17')
    # pass values
    low_bot = rules[p][0]
    high_bot = rules[p][1]

    if e1 < e2:
        if low_bot in bots:
            bots[low_bot].append(e1)
            if len(bots[low_bot]) >= 2:
                process_stack.append(low_bot)
        else:
            bots[low_bot] = [e1]

        if high_bot in bots:
            bots[high_bot].append(e2)
            if len(bots[high_bot]) >= 2:
                process_stack.append(high_bot)
        else:
            bots[high_bot] = [e2]

    else: # e1 > e2
        if high_bot in bots:
            bots[high_bot].append(e1)
            if len(bots[high_bot]) >= 2:
                process_stack.append(high_bot)
        else:
            bots[high_bot] = [e1]
        
        if low_bot in bots:
            bots[low_bot].append(e2)
            if len(bots[low_bot]) >= 2:
                process_stack.append(low_bot)
        else:
            bots[low_bot] = [e2]

#print(bots)

# part 2
print('part 2', bots[300][0] * bots[301][0] * bots[302][0])

# multiply the state of bot 300, 301, 302
