from typing import List, Set, Tuple


with open('Day19/input.txt') as f:
    
    replacements_text, txt = f.read().split('\n\n')


replacements: List[Tuple[str,str]] = []
for line in replacements_text.split('\n'):
    line = line.split()
    replacements.append((line[0],line[2]))


a: Set[str] = set()

import re

# for each replacement
for k,v in replacements:
    #  for each match
    for x in re.finditer(k,txt):
        # replace it and add it to the set
        a.add(txt[:x.start()]+v+txt[x.end():])
        
# the number of distinct molecules
print('Part 1:',len(a))
