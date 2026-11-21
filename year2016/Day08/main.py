

import re
from time import sleep
from typing import Tuple, cast

import numpy as np

animate = False
frame_length = 0.02


rect_rule = re.compile('rect (\\d+)x(\\d+)')
rotate_rule = re.compile('rotate (row y|column x)=(\\d+) by (\\d+)')

rows = 6
cols = 50
screen = np.ndarray((cols,rows),np.bool)

def print_screen():
    print('\033[6A',end='')
    for line in screen.transpose():
        linestr = ''.join(["█" if cell else " " for cell in line])
        print(linestr)
    
with open('Day08/input.txt') as f:
    if animate:
        print('\n\n\n\n\n\n',end='')
    for line in f:
        line = line.strip()
        m = rect_rule.fullmatch(line)
        if m is not None:
            # rect
            a,b = cast(Tuple[str,str],m.groups(m))
            a = int(a)
            b = int(b)
            for i in range(a):
                for j in range(b):
                    screen[i,j] = True
            if animate:
                print_screen()
                sleep(frame_length)
            continue

        m = rotate_rule.fullmatch(line)
        if m is not None:
            # rotate
            rc, p, s = cast(Tuple[str,str,str],m.groups(m))
            p = int(p)
            s = int(s)
            if rc.startswith('c'):
                # column
                # print(f'col {p} {s}\033[1A')
                data = screen[p,:].copy()
                for i,c in enumerate(data,s):
                    screen[p,i%rows] = c
                pass
            else:
                # row
                # print(f'row {p} {s}\033[1A')
                # get the old data for that row
                data = screen[:,p].copy()
                for i,c in enumerate(data,s):
                    screen[i%cols,p] = c

                pass
            if animate:
                print_screen()
                sleep(frame_length)
            continue
        print(f'could not match line {line}')
        exit(1)


print('Part 1:', screen.sum())
print('Part 2:')
print('\n\n\n\n\n\n',end='')
print_screen()

# as interesting as figuring out what letters are here know ing that it is a 5x6 font
# the easiest way is knowing what all the letters are, which I don't.
# I could guess at all the font letters, or try some sort of logic is this cell filled logic
# wow would both of those methods take a long time.
