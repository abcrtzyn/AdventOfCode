from typing import List, Tuple

replacements: List[Tuple[str,str]] = []

with open('replacements.txt') as f:
    for line in f.readlines():
        line = line.split()
        replacements.append((line[0],line[2]))

# print(replacements)
a = set()

import re
# part 1 is all about finding the keys, no need to do any replacements yet
with open('text.txt') as f:
    txt = f.readline()


    
for k,v in replacements:
    for x in re.finditer(k,txt):
        #print(x)

        a.add(txt[:x.start()]+v+txt[x.end():])
        
#print(a)
print(len(a))



