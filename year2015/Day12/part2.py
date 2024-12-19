import json

js = json.load(open('Day12/input.txt'))

def parselist(l):
    score = 0
    for item in l:
        if type(item) == list:
            score += parselist(item)
        elif type(item) == dict:
            score += parsedict(item)
        elif type(item) == str:
            pass
        elif type(item) == int:
            score += item
    return score


def parsedict(o: dict):
    score = 0
    for v in o.values():
        if type(v) == list:
            score += parselist(v)
        elif type(v) == dict:
            score += parsedict(v)
        elif type(v) == str:
            if v == 'red':
                return 0
        elif type(v) == int:
            score += v
    
    return score



if type(js) == list:
    print('Part 2:',parselist(js))
else:
    # I assume this will never be used
    print('Part 2:',parsedict(js))
    