import json

js = json.load(open('Day12/input.txt'))

def parselist(l):
    score = 0
    for item in l:
        #print(type(item))
        if type(item) == list:
            score += parselist(item)
        elif type(item) == dict:
            #print('object')
            score += parsedict(item)
            # parsedict(item)
        elif type(item) == str:
            pass
        elif type(item) == int:
            score += item
    return score

def parsedict(o):
    score = 0
    for k, v in o.items():
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


print(parselist(js))
    