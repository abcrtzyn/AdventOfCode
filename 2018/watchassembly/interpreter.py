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


ops = {f.__name__:f for f in [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]}



regs = [0,0,0,0,0,0]

ip = 5

program = []


with open('Day21/program.txt') as f:
    line = next(f)
    if line[0] == '#':
        # parse as ip directive
        ip = int(line[4])
    else:
        f.seek(0)
        
    
    for line in f:
        txt = line.strip().split(' ')
        program.append((txt[0],int(txt[1]),int(txt[2]),int(txt[3])))
        



while 0 <= regs[ip] < len(program):
    inst,a,b,c = program[regs[ip]]
    res = ops[inst](regs,a,b)
    regs[c] = res
    
    regs[ip] += 1


print(regs)
