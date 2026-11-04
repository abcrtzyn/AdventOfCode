import json
from typing import Dict, List, Union


JsonScalar = Union[str, int, float, bool, None]

JsonType = Union[
    JsonScalar,
    List["JsonType"],
    Dict[str, "JsonType"]
]




js: List[JsonType] | Dict[str,JsonType] = json.load(open('Day12/input.txt'))

def parselist(l: List[JsonType]) -> int:
    score: int = 0
    for item in l:
        if isinstance(item,list):
            score += parselist(item)
        elif isinstance(item,dict):
            score += parsedict(item)
        elif isinstance(item,str):
            pass
        elif isinstance(item,int):
            score += item
    return score


def parsedict(o: dict[str,JsonType]) -> int:
    score = 0
    for v in o.values():
        if isinstance(v,list):
            score += parselist(v)
        elif isinstance(v,dict):
            score += parsedict(v)
        elif isinstance(v,str):
            if v == 'red':
                return 0
        elif isinstance(v,int):
            score += v
    
    return score



if isinstance(js,list):
    print('Part 2:',parselist(js))
else:
    # I assume this will never be used
    print('Part 2:',parsedict(js))
    