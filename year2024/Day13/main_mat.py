# this solution does not compute part 2 correctly
# this one uses numpy linalg solve. Part 2 does not provide enough precision

import re
import numpy as np

button_line = re.compile('Button (A|B): X\\+(\\d+), Y\\+(\\d+)')
prize_line = re.compile('Prize: X=(\\d+), Y=(\\d+)')

tokens_used_1 = 0
# tokens_used_2 = 0
# part_2_offset = 10000000000000

def solve(ax,ay,bx,by,px,py):
    a = np.array([[ax,bx],[ay,by]],dtype=np.float64)
    b = np.array([px,py],dtype=np.float64)

    return np.linalg.solve(a,b)
    

with open('Day13/test_input.txt') as f:
    while True:

        line1 = button_line.match(f.readline())
        line2 = button_line.match(f.readline())
        line3 = prize_line.match(f.readline())
        if line1 is None or line2 is None or line3 is None:
            print('could not parse the input properly')
            exit(1)

        
        sol1 = solve(int(line1.group(2)),int(line1.group(3)),int(line2.group(2)),int(line2.group(3)),int(line3.group(1)),int(line3.group(2)))

        if np.isclose(sol1,sol1.round()).all():
            # add to tokens
            tokens_used_1 += np.sum(np.multiply(sol1,[3,1]))

        # sol2 = solve(int(line1.group(2)),int(line1.group(3)),int(line2.group(2)),int(line2.group(3)),int(line3.group(1))+part_2_offset,int(line3.group(2))+part_2_offset)
        # # print(sol2)
        # if np.isclose(sol2,sol2.round()).all():
        #     # add to tokens
        #     print(sol2)
        #     tokens_used_2 += np.sum(np.multiply(sol2,[3,1]))


        if f.readline() == '':
            break

print('Part 1:', int(tokens_used_1))
# print('Part 2:', int(tokens_used_2))
