import re

pat = re.compile('(do\\(\\))|(don\'t\\(\\))|(mul\\((\\d{1,3}),(\\d{1,3})\\))')


with open('Day03/input.txt') as f:
    entries = pat.findall(f.read())
    # only the current entry will be shown, one of the three
    # ('do()', 'don't()', 'mul()','2','4')

    # iterating through the entries one by one in order
    acc = 0
    enabled = True
    for entry in entries:
        if entry[0]:
            # if it is do()
            enabled = True
        elif entry[1]:
            # if it is don't()
            enabled = False
        elif enabled:
            # if it is mul() and we are enabled
            acc += int(entry[3]) * int(entry[4])

print('Part 2:',acc)
