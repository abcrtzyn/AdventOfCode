import re
from typing import Dict, List, Tuple, cast

rule = re.compile('(set|sub|mul|jnz) (-?\\d+|[a-z]) ?(-?\\d+|[a-z])?')

program: List[Tuple[str,str|int,str|int|None]] = []


with open('Day23/input.txt') as f:
    for line in f.readlines():
        mat = rule.match(line)
        if mat is None:
            print(f'could not match line "{line}"')
            exit(1)
        res = cast(Tuple[str,str,str|None], mat.groups())
        
        if res[1][-1].isdigit():
            # its a number
            res = (res[0],int(res[1]),res[2])
        
        if True:
            if res[2] is None:
                print(f'argument two not parsed in line "{line}"')
                exit()
            
            if res[2][-1].isdigit():
                res = (res[0],res[1],int(res[2]))

        program.append(res)


# interpret the program

prog_counter = 0
registers: Dict[str,int] = {}
mul_count = 0
# instruction_count = {'set':0,''}


try:
    while True:
        line = program[prog_counter]
        #print(line, registers)
        op = line[0]
        arg1 = line[1]
        arg2 = line[2]

        match op:
            case 'set':
                assert isinstance(arg1,str)
                if isinstance(arg2,int):
                    registers[arg1] = arg2
                else:
                    if arg2 in registers:
                        registers[arg1] = registers[arg2]
                    else:
                        registers[arg1] = 0
            case 'sub':
                assert isinstance(arg1,str)
                if arg2 in registers:
                    value = registers[arg2]
                else:
                    assert isinstance(arg2,int)
                    value = arg2
                
                if arg1 in registers:
                    registers[arg1] -= value
                else:
                        registers[arg1] = value
            case 'mul':
                assert isinstance(arg1,str)
                mul_count += 1
                if arg2 in registers:
                    value = registers[arg2]
                else:
                    assert isinstance(arg2,int)
                    value = arg2
                
                if arg1 in registers:
                    registers[arg1] *= value
                else:
                        registers[arg1] = value
            case 'jnz':
                if arg2 in registers:
                    value = registers[arg2] - 1
                else:
                    assert isinstance(arg2,int)
                    value = arg2 - 1

                if isinstance(arg1,int):
                    if arg1 != 0:
                        prog_counter += value
                else:
                    if arg1 in registers and registers[arg1] != 0:
                        prog_counter += value
            case _:
                assert False, 'unreachable'
            
        prog_counter += 1
except Exception as e:
    print('mul_count',mul_count)
    #raise e
