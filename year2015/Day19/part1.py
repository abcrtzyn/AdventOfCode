from typing import List, Tuple

replacements: List[Tuple[str,str]] = []

with open('Day19/replacements.txt') as f:
    for line in f:
        line = line.split()
        replacements.append((line[0],line[2]))

# print(replacements)
a = set()

import re

with open('Day19/text.txt') as f:
    txt = f.readline()


# for each replacement
for k,v in replacements:
    #  for each match
    for x in re.finditer(k,txt):
        # replace it and add it to the set
        a.add(txt[:x.start()]+v+txt[x.end():])
        
# the number of distinct molecules
print('Part 1:',len(a))
