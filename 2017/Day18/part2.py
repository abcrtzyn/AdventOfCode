import re
from typing import List, Dict

rule = re.compile('(snd|set|add|mul|mod|rcv|jgz) (-?\\d+|[a-z]) ?(-?\\d+|[a-z])?')




program = []

queueA = []
queueB = []


class Program:
    # registers: Dict[str,int] = {}
    # prog_counter = 0

    def __init__(self,number: int,sndqueue: List[int],rcvqueue: List[int]):
        self.registers: Dict[str,int] = {}
        self.prog_counter = 0
        self.registers['p'] = number
        self.sndqueue: List[int] = sndqueue
        self.rcvqueue: List[int] = rcvqueue
        self.snd_count = 0
    
    def run(self):
        while True:
            line = program[self.prog_counter]
            #print(line, self.registers)

            match line[0]:
                case 'set':
                    if type(line[2]) == int:
                        self.registers[line[1]] = line[2]
                    else:
                        if line[2] in self.registers:
                            self.registers[line[1]] = self.registers[line[2]]
                        else:
                            self.registers[line[1]] = 0
                case 'add':
                    if line[2] in self.registers:
                        value = self.registers[line[2]]
                    else:
                        value = line[2]
                    
                    if line[1] in self.registers:
                        self.registers[line[1]] += value
                    else:
                         self.registers[line[1]] = value
                case 'mul':
                    if line[2] in self.registers:
                        value = self.registers[line[2]]
                    else:
                        value = line[2]
                    
                    if line[1] in self.registers:
                        self.registers[line[1]] *= value
                    else:
                         self.registers[line[1]] = value
                case 'mod':
                    if line[2] in self.registers:
                        value = self.registers[line[2]]
                    else:
                        value = line[2]
                    
                    if line[1] in self.registers:
                        self.registers[line[1]] %= value
                    else:
                         self.registers[line[1]] = value
                case 'jgz':
                    if line[2] in self.registers:
                        value = self.registers[line[2]] - 1
                    else:
                        value = line[2] - 1

                    if type(line[1]) == int:
                        if line[1] > 0:
                            self.prog_counter += value
                    else:
                        if self.registers[line[1]] > 0:
                            self.prog_counter += value
                case 'snd':
                    if line[1] in self.registers:
                        self.sndqueue.append(self.registers[line[1]])
                    else:
                        self.sndqueue.append(line[1])
                    self.snd_count += 1
                case 'rcv':
                    if len(self.rcvqueue) > 0:
                        self.registers[line[1]] = self.rcvqueue.pop(0)
                    else:
                        return
            self.prog_counter += 1




with open('Day18/input.txt') as f:
    for line in f.readlines():
        mat = rule.match(line)
        if mat is None:
            print(f'could not match line "{line}"')
            exit(1)
        res = mat.groups()
        
        if res[1][-1].isdigit():
            # its a number
            res = (res[0],int(res[1]),res[2])
        
        if res[0] != 'snd' and res[0] != 'rcv':
            if res[2] is None:
                print(f'argument two not parsed in line "{line}"')
            
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
