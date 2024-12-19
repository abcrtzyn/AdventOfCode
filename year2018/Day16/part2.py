

import re


def addr(registers,a,b):
    return registers[a] + registers[b]

def addi(registers,a,b):
    return registers[a] + b

def mulr(registers,a,b):
    return registers[a] * registers[b]

def muli(registers,a,b):
    return registers[a] * b

def banr(registers,a,b):
    return registers[a] & registers[b]

def bani(registers,a,b):
    return registers[a] & b

def borr(registers,a,b):
    return registers[a] | registers[b]

def bori(registers,a,b):
    return registers[a] | b

def setr(registers,a,b):
    return registers[a]

def seti(registers,a,b):
    return a

def gtir(registers,a,b):
    return 1 if a > registers[b] else 0

def gtri(registers,a,b):
    return 1 if registers[a] > b else 0

def gtrr(registers,a,b):
    return 1 if registers[a] > registers[b] else 0

def eqir(registers,a,b):
    return 1 if a == registers[b] else 0

def eqri(registers,a,b):
    return 1 if registers[a] == b else 0

def eqrr(registers,a,b):
    return 1 if registers[a] == registers[b] else 0

ops = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]






sample_rule = re.compile('Before: \\[(\\d+), (\\d+), (\\d+), (\\d+)\\]\n(\\d+) (\\d+) (\\d+) (\\d+)\nAfter:  \\[(\\d+), (\\d+), (\\d+), (\\d+)\\]')

samples = []





with open('Day16/samples.txt') as f:
    samplestxt = f.read().split('\n\n')

    for s in samplestxt:
        mat = sample_rule.match(s)
        if mat is None:
            print('could not parse sample')
            exit(1)
        samples.append(tuple([int(x) for x in mat.groups()]))

lots_of_possibles = 0

from itertools import groupby

maps = {}


for k,ss in groupby(samples,(lambda x: x[4])):
    # print(k)
    possibles = set([f.__name__ for f in ops])
    
    for s in ss:
        regs = (s[0],s[1],s[2],s[3])
        instruction = s[4]
        a = s[5]
        b = s[6]
        c = s[7]
        out = (s[8],s[9],s[10],s[11])
        
        for f in ops:
            if f(regs,a,b) != out[c]:
                possibles.discard(f.__name__)
        if len(possibles) == 1:
            break
    
    if len(possibles) == 1:
        maps[k] = possibles.pop()
    elif len(possibles) > 1:
        maps[k] = possibles.copy()
    else:
        print('bug')
        exit(1)

print(maps)

# elimination will be faster by hand
# 10: 'eqrr', 
# 2: {'seti', 'addr'}, 
# 9: {'eqrr', 'eqri'}, 
# 12: {'gtir', 'setr'}, 
# 3: {'gtri', 'eqir', 'eqrr'}, 
# 14: {'seti', 'addr', 'addi'}, 
# 0: {'eqrr', 'eqir', 'eqri'}, 
# 13: {'gtri', 'eqir', 'gtrr', 'eqri'}, 
# 5: {'gtri', 'eqir', 'gtir', 'eqri', 'eqrr', 'gtrr'}, 
# 7: {'gtri', 'eqir', 'gtir', 'eqri', 'eqrr', 'gtrr', 'banr'}, 
# 1: {'seti', 'eqir', 'borr', 'setr', 'eqrr', 'banr', 'mulr', 'bani'},
# 6: {'gtri', 'seti', 'eqri', 'eqrr', 'gtir', 'banr', 'mulr', 'bani'}}
# 11: {'gtri', 'eqir', 'eqri', 'eqrr', 'gtir', 'banr', 'gtrr', 'bani'}, 
# 15: {'gtri', 'seti', 'eqir', 'eqri', 'eqrr', 'gtir', 'banr', 'gtrr', 'bani'}, 
# 8: {'gtri', 'seti', 'eqir', 'borr', 'setr', 'eqrr', 'banr', 'bori', 'mulr', 'addi'}, 
# 4: {'gtri', 'seti', 'borr', 'setr', 'gtir', 'addr', 'banr', 'muli', 'bori', 'gtrr', 'mulr', 'bani', 'addi'}, 

# 10: eqrr
# 9:  eqri
# 0:  eqir
# 3:  gtri
# 13: gtrr
# 5:  gtir
# 12: setr
# 7:  banr
# 11: bani
# 15: seti
# 2:  addr
# 14: addi
# 6:  mulr
# 1:  borr
# 8:  bori
# 4:  muli
