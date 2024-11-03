from typing import List, Tuple

replacements_backwards: List[Tuple[str,str]] = []
replacements_forward: List[Tuple[str,str]] = []

with open('replacements.txt') as f:
    for line in f.readlines():
        line = line.split()
        if line[2].find('CRn') == -1: # these replacements do nothing in part 2.
            replacements_forward.append((line[0],line[2]))
            replacements_backwards.append((line[2],line[0])) # swap the replacements


import re



# prefix = ''
# with open('text_splits.txt') as f:
#     for line in f.readlines():
#         line = prefix + line.strip()
#         # simplify the line
        


# exit()
# find first Rn Ar pair


# im just going to do alot of this manually

# # starting with txt
# # try each replacement on each location
a = {}


a['HCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnFYFArSiRnFYFArPTiRnFArSiRnFArRnFArCaSiRnFYFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnFArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnMgArCaSiRnFArRnFArSiRnFArTiRnFArF'] = 0

i = 0
while True:
    na = set()
    for s in a: # for each string in the iteration
        if a[s] == i:
            for k,v in replacements_backwards: # for each replacement
                for x in re.finditer(k,s): # for each location in replacement
                    #print(x)
                    ns = s[:x.start()]+v+s[x.end():]
                    if ns not in a:
                        na.add(s[:x.start()]+v+s[x.end():]) # add the replaced string to the set (if it doesn't exist already)
    
    # one more replacement has been done
    i += 1
    print(i, len(na))
    if 'e' in na:
        print('got e')
        break

    for s in na:
        a[s] = i
    

if 'Mg' in a:
    print('Mg')
if 'F' in a:
    print('F')