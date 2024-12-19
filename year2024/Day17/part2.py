# this program attempts each program iteration in reverse to find the next output digit
# assumes that every program is set up like the following
# assumes all values of B and C are assigned each iteration

# B <- A % 8    get the last three bits of A
# do some processing
# A <- A >> 3   shift A by three bits
# do some more processing
# Output B
# If A != 0, go back to the beginning





# parse the input
with open('Day17/input.txt') as f:
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    program = [int(x) for x in f.readline()[9:].split(',')]
    output = program.copy()

reg_a = 0
reg_b = 0
reg_c = 0

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

# to end the program, A is 0, so we start with A=0
new_possibles = [0]

while output:

    possibles = new_possibles
    new_possibles = []
    # target value is the last value outputed
    target = output.pop()

    # for each valid value
    for v in possibles:
        # for each 3 bit value
        for i in range(8):
            # try to extend A with each 3 bit value
            reg_a = (v << 3) + i

            # simulate one iteration of the program
            # it stops on the output
            ip = 0
            while True:
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
                        # if it is the same as what the output should be, mark it as a valid value
                        # and stop simulating
                        if combo(operand) % 8 == target:
                            new_possibles.append((v << 3) + i)
                        break
                        
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

    
print('Part 2:', min(new_possibles))
