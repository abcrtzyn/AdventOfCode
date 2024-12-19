

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


for s in samples:
    regs = (s[0],s[1],s[2],s[3])
    instruction = s[4]
    a = s[5]
    b = s[6]
    c = s[7]
    out = (s[8],s[9],s[10],s[11])
    
    possibles = 0

    for f in ops:
        if f(regs,a,b) == out[c]:
            possibles += 1

    if possibles >= 3:
        lots_of_possibles += 1

print(lots_of_possibles)
