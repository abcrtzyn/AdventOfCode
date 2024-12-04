import re

pat = re.compile('(do\\(\\))|(don\'t\\(\\))|(mul\\((\\d{1,3}),(\\d{1,3})\\))')


with open('Day03/input.txt') as f:
    entries = pat.findall(f.read())
    # print(entries)
    acc = 0
    enabled = True
    for entry in entries:
        if entry[0]:
            enabled = True
        elif entry[1]:
            enabled = False
        elif enabled:
            acc += int(entry[3]) * int(entry[4])

print('Part 2:',acc)
