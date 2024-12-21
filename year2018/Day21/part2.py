# this part requires lots of knowledge of how the program works.
# my guess is that every input is nearly the same program with different numbers

# this program requires the following to be true
# the final comparison of the program is with register 3
# this compaison occurs on line 28
# starting at line 17 is a routine to divide by 256 and then goes to line 8

# the input program computes a sequence of values and compares r0 to each number
# in order to find the right value of r0, the program must find 
# the value in the sequence just before the sequence repeats any values


from year2018.watchassembly.interpreter import parse, ops


regs = [0,0,0,0,0,0]

ip = 5

program = []





with open('Day21/input.txt') as f:
    program, ip = parse(f)

assert type(ip) == int

values = set()
previous = 0

while 0 <= regs[ip] < len(program):
    if regs[ip] == 28:
        v = regs[3]
        if v in values:
            print('Part 2:', previous)
            exit(0)
        else:
            previous = v
            values.add(v)

    # skipping a bunch of steps to speed it up
    # turns out that was enough optimization
    if regs[ip] == 17:
        regs[2] = regs[2]>>8
        regs[ip] = 8

    inst,a,b,c = program[regs[ip]]
    res = ops[inst](regs,a,b)
    regs[c] = res
    
    regs[ip] += 1
