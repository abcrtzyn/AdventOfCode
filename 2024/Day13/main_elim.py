# time for some algebra
# this solution uses elimination and integers
# integers keep precision, plus Python has very large integers


import re
from typing import Optional, Tuple

button_line = re.compile('Button (A|B): X\\+(\\d+), Y\\+(\\d+)')
prize_line = re.compile('Prize: X=(\\d+), Y=(\\d+)')

tokens_used_1 = 0
tokens_used_2 = 0
part_2_offset = 10000000000000

def solve(ax:int,ay:int,bx:int,by:int,px:int,py:int) -> Optional[Tuple[int,int]]:
    # solving the system using elimination... and integers
    # a solution that does not have an integer solution returns None

    # subtract one from the other, ax and ay cancel
    py = (py * ax) - (px * ay)
    by = (by * ax) - (bx * ay)
    # now py = by * B
    # if the remainder of division is not 0, it is not an integer solution
    if py % by != 0:
        return None
    
    B = py // by

    # use px and bx to get A
    val = px - bx * B
    if val % ax != 0:
        # unlikely code
        return None

    A = val // ax

    return (A,B)



with open('Day13/input.txt') as f:
    while True:

        line1 = button_line.match(f.readline())
        line2 = button_line.match(f.readline())
        line3 = prize_line.match(f.readline())
        if line1 is None or line2 is None or line3 is None:
            print('could not parse the input properly')
            exit(1)

        
        sol1 = solve(int(line1.group(2)),int(line1.group(3)),int(line2.group(2)),int(line2.group(3)),int(line3.group(1)),int(line3.group(2)))

        if sol1 is not None:
            tokens_used_1 += 3*sol1[0] + sol1[1]

        sol2 = solve(int(line1.group(2)),int(line1.group(3)),int(line2.group(2)),int(line2.group(3)),int(line3.group(1))+part_2_offset,int(line3.group(2))+part_2_offset)

        if sol2 is not None:
            tokens_used_2 += 3*sol2[0] + sol2[1]        

        if f.readline() == '':
            break

print('Part 1:', int(tokens_used_1))
print('Part 2:', int(tokens_used_2))
