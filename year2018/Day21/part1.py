from year2018.watchassembly.interpreter import interpret, parse

# from following the code, running the program up to 3 lines gives the value that r0 must equal
# r0 does not change throughout the program and is only used to compare to on the third to last line



with open('Day21/input.txt') as f:
    program, ip_reg = parse(f)

    assert type(ip_reg) == int

    # checking the input for cases that I don't have
    compare_instr = program[-3]
    if compare_instr[0] != 'eqrr':
        print(compare_instr)
        print('this doesn\'t look right, there should be a equals reg reg instruction here')
        exit(1)
    # one of arg 1 or arg 2 is zero, the other is the value we need
    needed_register = 0
    if compare_instr[1] == 0:
        needed_register = compare_instr[2]
    elif compare_instr[2] == 0:
        needed_register = compare_instr[1]
    else:
        print(compare_instr)
        print('expected a register comparison between r0 and another register')
        exit(1)

    program = program[:-2]
    
    print('Part 1:',interpret(program,ip_reg=ip_reg)[needed_register])
