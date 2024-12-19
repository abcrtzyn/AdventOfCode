# this program inteprets the program

print('Part 1: ',end='')


# parse the input
with open('Day17/test_input2.txt') as f:
    reg_a = int(f.readline()[12:])
    reg_b = int(f.readline()[12:])
    reg_c = int(f.readline()[12:])

    f.readline()
    program = [int(x) for x in f.readline()[9:].split(',')]


def combo(operand: int) -> int:
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return reg_a
        case 5:
            return reg_b
        case 6:
            return reg_c
        case _:
            raise ValueError(operand,'not a vaild combo operand')


ip = 0

while True:
    # print(reg_a,reg_b,reg_c)
    if not (0 <= ip < len(program)):
        break
    
    instruction = program[ip]
    operand = program[ip+1]
    # print(instruction, operand)
    ip += 2
    match instruction:
        case 1:
            # BXL
            # print('BXL')
            # print(bin(reg_b),bin(operand),bin(reg_b^operand))
            reg_b = reg_b ^ operand
        case 2:
            # BST
            # print('BST')
            # print(bin(combo(operand)))
            # print(bin(combo(operand) % 8))
            # print(bin(combo(operand) & 7))
            reg_b = combo(operand) & 0b111
        case 3:
            # JNZ
            if reg_a != 0:
                ip = operand
        case 4:
            # BXC
            reg_b = reg_b ^ reg_c
        case 5:
            # OUT
            print(combo(operand) & 0b111,end=',')
        case 0:
            # ADV
            reg_a = reg_a >> combo(operand)
            # numerator = reg_a
            # denominator = 2 ** combo(operand)
            # # print(denominator)
            # reg_a = numerator // denominator # truncated
        case 6:
            # BDV
            reg_b = reg_a >> combo(operand)
            # numerator = reg_a
            # denominator = 2 ** combo(operand)
            # reg_b = numerator // denominator # truncated
        case 7:
            # CDV
            # numerator = reg_a
            # denominator = 2 ** combo(operand)
            reg_c = reg_a >> combo(operand)
            # reg_c = numerator // denominator # truncated

        case _:
            print('unknown instruction', instruction)
            exit(1)

print('\b ')
