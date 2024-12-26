values = {}


with open('Day24/input.txt') as f:
    mode = 0
    for line in f:
        line = line.strip()
        if line == '':
            mode += 1
            continue
    
        if mode == 0:
            name, valstr = line.split(':')
            values[name] = int(valstr)
        elif mode == 1:
            exp, name = line.split(' -> ')
            values[name] = exp


def evaluate(name) -> int:
    if type(values[name]) == int:
        return values[name]
    
    exp1, op, exp2 = values[name].split(' ')
    v1 = evaluate(exp1)
    v2 = evaluate(exp2)
    
    match op:
        case 'AND':
            ret = v1 & v2
        case 'XOR':
            ret = v1 ^ v2
        case 'OR':
            ret = v1 | v2
        case _:
            raise ValueError('unknown operation f{op}')
    
    values[name] = ret

    return ret
    



result = 0

i = 0
while True:
    name = f'z{i:02d}'
    if name in values:
        result += evaluate(name) * 2**i
    else:
        break
    i += 1

print(result)
