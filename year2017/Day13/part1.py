

# camera cycles are 2s-2
# when the cycle lines up with the layer number, the packet is caught

import re
rule = re.compile('(\\d+): (\\d+)')

penalty = 0

with open('Day13/input.txt') as f:
    for line in f.readlines():
        mat = rule.match(line)
        if mat is None:
            print('could not match line')
            exit(1)
        
        if int(mat.group(1)) % (2*int(mat.group(2))-2) == 0:
            penalty += int(mat.group(1)) * int(mat.group(2))

print(penalty)
