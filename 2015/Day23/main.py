
# emulate the program and return the state
def emulate(prog, a, b):
    prog_len = len(prog)
    pc = 0
    while True:
        #print(a)
        if pc >= prog_len:
            break

        x = prog[pc]
        #print(x)
        match x[0]:
            case 'jio':
                # jump if one
                if x[1] == 'a,':
                    if a == 1:
                        pc += int(x[2])
                    else:
                        pc += 1
                else:
                    raise Exception('not imp',x[1])
            case 'inc':
                if x[1] == 'a':
                    a += 1
                elif x[1] == 'b':
                    b += 1
                else:
                    raise Exception('not imp',x[1])
                pc += 1
            case 'tpl':
                if x[1] == 'a':
                    a *= 3
                else:
                    raise Exception('not imp',x[1])
                pc += 1
            case 'jmp':
                pc += int(x[1])
            case 'jie':
                # jump if even
                assert x[1] == 'a,'
                if a % 2 == 0:
                    pc += int(x[2])
                else:
                    pc += 1
            case 'hlf':
                assert x[1] == 'a'
                a /= 2
                pc += 1
            case _:
                raise Exception(x[0])
    
    return (a,b)

with open('Day23/input.txt') as f:
    lines = [x.strip().split() for x in f.readlines()]
    

print('Part 1:', emulate(lines,0,0)[1])
print('Part 2:', emulate(lines,1,0)[1])
