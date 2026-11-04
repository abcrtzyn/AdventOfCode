from typing import Dict, List, TextIO, Tuple


def addr(registers: List[int],a: int,b: int) -> int:
    return registers[a] + registers[b]

def addi(registers: List[int],a: int,b: int) -> int:
    return registers[a] + b

def mulr(registers: List[int],a: int,b: int) -> int:
    return registers[a] * registers[b]

def muli(registers: List[int],a: int,b: int) -> int:
    return registers[a] * b

def banr(registers: List[int],a: int,b: int) -> int:
    return registers[a] & registers[b]

def bani(registers: List[int],a: int,b: int) -> int:
    return registers[a] & b

def borr(registers: List[int],a: int,b: int) -> int:
    return registers[a] | registers[b]

def bori(registers: List[int],a: int,b: int) -> int:
    return registers[a] | b

def setr(registers: List[int],a: int,b: int) -> int:
    return registers[a]

def seti(registers: List[int],a: int,b: int) -> int:
    return a

def gtir(registers: List[int],a: int,b: int) -> int:
    return 1 if a > registers[b] else 0

def gtri(registers: List[int],a: int,b: int) -> int:
    return 1 if registers[a] > b else 0

def gtrr(registers: List[int],a: int,b: int) -> int:
    return 1 if registers[a] > registers[b] else 0

def eqir(registers: List[int],a: int,b: int) -> int:
    return 1 if a == registers[b] else 0

def eqri(registers: List[int],a: int,b: int) -> int:
    return 1 if registers[a] == b else 0

def eqrr(registers: List[int],a: int,b: int) -> int:
    return int(registers[a] == registers[b])


ops = {f.__name__:f for f in [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]}


def interpret(program: List[Tuple[str,int,int,int]], initial_regs: List[int] = [0,0,0,0,0,0], ip_reg:int=5):
    regs = initial_regs

    while 0 <= regs[ip_reg] < len(program):
        inst,a,b,c = program[regs[ip_reg]]
        res = ops[inst](regs,a,b)
        regs[c] = res
        
        regs[ip_reg] += 1

    return regs


def parse(f: TextIO, dissasemble_map: Dict[int,str] | None=None) -> Tuple[List[Tuple[str, int, int, int]],int|None]:
    program: List[Tuple[str, int, int, int]] = []

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
