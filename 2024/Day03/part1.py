import re

pat = re.compile('mul\\((\\d{1,3}),(\\d{1,3})\\)')


with open('Day03/input.txt') as f:
    # find all gives tuples of each group, ('2', '4')
    entries = pat.findall(f.read())

    print('Part 1:',sum(int(x)*int(y) for x, y in entries))
