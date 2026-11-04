import re
from typing import List, Dict, Tuple, cast

rule = re.compile('(snd|set|add|mul|mod|rcv|jgz) (-?\\d+|[a-z]) ?(-?\\d+|[a-z])?')




program: List[Tuple[str,str|int,str|int|None]] = []

queueA: List[int] = []
queueB: List[int] = []


class Program:
    # registers: Dict[str,int] = {}
    # prog_counter = 0

    def __init__(self,number: int,sndqueue: List[int],rcvqueue: List[int]):
        self.registers: Dict[str,int] = {}
        self.prog_counter: int = 0
        self.registers['p'] = number
        self.sndqueue: List[int] = sndqueue
        self.rcvqueue: List[int] = rcvqueue
        self.snd_count = 0
    
    def run(self):
        while True:
            line = program[self.prog_counter]
            #print(line, self.registers)
            op = line[0]
            arg1 = line[1]
            arg2 = line[2]

            match op:
                case 'set':
                    assert isinstance(arg1,str)
                    if isinstance(arg2,int):
                        self.registers[arg1] = arg2
                    else:
                        if arg2 in self.registers:
                            self.registers[arg1] = self.registers[arg2]
                        else:
                            self.registers[arg1] = 0
                case 'add':
                    assert isinstance(arg1,str)
                    if arg2 in self.registers:
                        value = self.registers[arg2]
                    else:
                        assert isinstance(arg2,int)
                        value = arg2
                    
                    if arg1 in self.registers:
                        self.registers[arg1] += value
                    else:
                         self.registers[arg1] = value
                case 'mul':
                    assert isinstance(arg1,str)
                    if arg2 in self.registers:
                        value = self.registers[arg2]
                    else:
                        assert isinstance(arg2,int)
                        value = arg2
                    
                    if arg1 in self.registers:
                        self.registers[arg1] *= value
                    else:
                         self.registers[arg1] = value
                case 'mod':
                    assert isinstance(arg1,str)
                    if arg2 in self.registers:
                        value = self.registers[arg2]
                    else:
                        assert isinstance(arg2,int)
                        value = arg2
                    
                    if arg1 in self.registers:
                        self.registers[arg1] %= value
                    else:
                         self.registers[arg1] = value
                case 'jgz':
                    if arg2 in self.registers:
                        value = self.registers[arg2] - 1
                    else:
                        assert isinstance(arg2,int)
                        value = arg2 - 1

                    if isinstance(arg1,int):
                        if arg1 > 0:
                            self.prog_counter += value
                    else:
                        if self.registers[arg1] > 0:
                            self.prog_counter += value
                case 'snd':
                    if arg1 in self.registers:
                        self.sndqueue.append(self.registers[arg1])
                    else:
                        assert isinstance(arg1,int)
                        self.sndqueue.append(arg1)
                    self.snd_count += 1
                case 'rcv':
                    assert isinstance(arg1,str)
                    if len(self.rcvqueue) > 0:
                        self.registers[arg1] = self.rcvqueue.pop(0)
                    else:
                        return
                case _:
                    assert False, 'unreachable'
            
            self.prog_counter += 1




with open('Day18/input.txt') as f:
    for line in f.readlines():
        mat = rule.match(line)
        if mat is None:
            print(f'could not match line "{line}"')
            exit(1)
        res = cast(Tuple[str,str,str|None],mat.groups())
        
        if res[1][-1].isdigit():
            # its a number
            res = (res[0],int(res[1]),res[2])
        
        if res[0] != 'snd' and res[0] != 'rcv':
            if res[2] is None:
                print(f'argument two not parsed in line "{line}"')
                exit()
            
            if res[2][-1].isdigit():
                res = (res[0],res[1],int(res[2]))

        
        program.append(res)



# create two programs, two seperate threads if im feeling fancy (im not feeling fancy)
prog0 = Program(0,queueA,queueB)
prog1 = Program(1,queueB,queueA)

while True:
    prog0.run()
    prog1.run()
    
    if len(queueB) == 0:
        # stuck
        break

print(prog1.snd_count)
