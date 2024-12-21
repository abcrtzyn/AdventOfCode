from io import TextIOBase
from typing import List, Tuple


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
    return int(registers[a] == registers[b])


ops = {f.__name__:f for f in [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]}


def interpret(program: List[Tuple[str,int,int,int]], initial_regs: List[int] = [0,0,0,0,0,0], ip_reg=5):
    regs = initial_regs

    while 0 <= regs[ip_reg] < len(program):
        inst,a,b,c = program[regs[ip_reg]]
        res = ops[inst](regs,a,b)
        regs[c] = res
        
        regs[ip_reg] += 1

    return regs


def parse(f: TextIOBase, dissasemble_map=None):
    program = []

    line = next(f)
    if line[0] == '#':
        # parse as ip directive
        ip_reg = int(line[4])
    else:
        ip_reg = None
        f.seek(0)
            
        
    for line in f:
        txt = line.strip().split(' ')
        opcode = dissasemble_map[int(txt[0])] if dissasemble_map is not None else txt[0]
        program.append((opcode,int(txt[1]),int(txt[2]),int(txt[3])))

    return program, ip_reg
