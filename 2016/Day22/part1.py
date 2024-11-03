# viable pairs
# it is 30x35 grid
# number of pairs to check 1050^2 = about 1,000,000
# good enough for brute force

from io import TextIOWrapper
from typing import Tuple, Dict
import re

line_rule = re.compile('/dev/grid/node-x(\\d+)-y(\\d+) +(\\d+)T +(\\d+)T +(\\d+)T +(\\d+)%')

grid: Dict[Tuple[int,int],Tuple[int,int,int,int]] = {}
SIZE = 0
USED = 1
AVAL = 2
PERC = 3


def read_lines(f: TextIOWrapper):
    while True:
        line = f.readline()
        if line == '':
            break
        yield line


with open('Day22/input.txt') as f:
    f.readline()
    f.readline()
    for line in read_lines(f):
        mat = line_rule.match(line)
        if mat is None:
            print(f'did not match "{line}"')
            exit(1)
        grid[(int(mat.group(1)),int(mat.group(2)))] = (int(mat.group(3)),int(mat.group(4)),int(mat.group(5)),int(mat.group(6)))

viable_count = 0

for a,ar in grid.items():
    for b,br in grid.items():
        if a == b:
            continue
        if ar[USED] == 0:
            continue
        if ar[USED] <= br[AVAL]:
            viable_count += 1

print(viable_count)
