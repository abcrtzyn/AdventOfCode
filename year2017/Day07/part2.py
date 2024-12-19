from typing import Dict, List

root = 'wiapj'


unit_weights: Dict[str,int] = {}
unit_subs: Dict[str,List[str]] = {}
# tower_weights = {}


import re

line_rule = re.compile('(?P<name>\\w+) \\((?P<weight>\\d+)\\)( -> (?P<subs>(\\w+(, )?)+))?')

with open('Day07/input.txt') as f:
    for line in f.readlines():
        mat = line_rule.match(line)
        if mat is None:
            print(f'did not match line "{line}"')
            exit(1)
        res: Dict[str,str] = mat.groupdict()
        if res['subs'] is not None:
            subs = res['subs']
            # parse subs
            subs = subs.split(', ')
        else:
            subs = []

        unit_weights[res['name']] = int(res['weight'])
        unit_subs[res['name']] = subs


# recursively fill in tower weights
# i dont suspect it will go over 997 function calls

def find_discrepency(unit:str):
    weight = unit_weights[unit]
    # get the weights of all the sub towers
    # also check if one of them is off

    sub_weights = [find_discrepency(s) for s in unit_subs[unit]]
    if len(sub_weights) > 0 and len(set(sub_weights)) != 1:
        # deal with the discrepency
        print(unit, unit_subs[unit], sub_weights)
        
    return unit_weights[unit] + sum(sub_weights)
    

find_discrepency(root)
