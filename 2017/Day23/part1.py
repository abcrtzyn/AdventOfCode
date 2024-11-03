import re
from typing import List, Dict

rule = re.compile('(set|sub|mul|jnz) (-?\\d+|[a-z]) ?(-?\\d+|[a-z])?')

program = []


with open('Day23/input.txt') as f:
    for line in f.readlines():
        mat = rule.match(line)
        if mat is None:
            print(f'could not match line "{line}"')
            exit(1)
        res = mat.groups()
        
        if res[1][-1].isdigit():
            # its a number
            res = (res[0],int(res[1]),res[2])
        
        if True:
            if res[2] is None:
                print(f'argument two not parsed in line "{line}"')
            
            if res[2][-1].isdigit():
                res = (res[0],res[1],int(res[2]))

        program.append(res)


# interpret the program

prog_counter = 0
registers = {}
mul_count = 0
# instruction_count = {'set':0,''}


try:
    while True:
        line = program[prog_counter]
        #print(line, registers)

        match line[0]:
            case 'set':
                if type(line[2]) == int:
                    registers[line[1]] = line[2]
                else:
                    if line[2] in registers:
                        registers[line[1]] = registers[line[2]]
                    else:
                        registers[line[1]] = 0
            case 'sub':
                if line[2] in registers:
                    value = registers[line[2]]
                else:
                    value = line[2]
                
                if line[1] in registers:
                    registers[line[1]] -= value
                else:
                        registers[line[1]] = value
            case 'mul':
                mul_count += 1
                if line[2] in registers:
                    value = registers[line[2]]
                else:
                    value = line[2]
                
                if line[1] in registers:
                    registers[line[1]] *= value
                else:
                        registers[line[1]] = value
            case 'jnz':
                if line[2] in registers:
                    value = registers[line[2]] - 1
                else:
                    value = line[2] - 1

                if type(line[1]) == int:
                    if line[1] != 0:
                        prog_counter += value
                else:
                    if line[1] in registers and registers[line[1]] != 0:
                        prog_counter += value
        prog_counter += 1
except Exception as e:
    print('mul_count',mul_count)
    #raise e
