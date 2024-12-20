# I will guess that all programs are set up in the same way with different numbers
# Line 0 jumps down to the third third of the program, it calculates a big number, and jumps to line 1
# The main bulk of the program calculates the sum of divisors of this big number

# I know what my big number is, but I don't know all the big numbers
# THIS PROGRAM IS A GUESS AND COULD YEILD THE WRONG ANSWER
# if the description above of the input program does not look like what your program does

# I figured this out by hand at first, it was pretty easy to look up the sum of divisors for a given number

from year2018.watchassembly.interpreter import interpret, parse


def sum_of_divisors(number):
    total = 0
    i = 1
    while i**2 <= number:
        if number % i == 0:
            total += i
            total += number // i
        i += 1
    
    return total


with open('Day19/input.txt') as f:
    program, ip = parse(f)
    assert type(ip) == int

# I want to know what the big number in r5 is at line 1, so exit the program at line 1
program[1] = ('seti', -10, 0, ip)

big_number_1 = interpret(program, ip_reg=ip)[5]
big_number_2 = interpret(program, initial_regs=[1,0,0,0,0,0], ip_reg=ip)[5]

# calculate the sum of divisors faster than the assembly program ever will
print('Part 1:',sum_of_divisors(big_number_1))
print('Part 2:',sum_of_divisors(big_number_2))
