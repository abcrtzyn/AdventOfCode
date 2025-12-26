from functools import reduce
from itertools import combinations
from operator import xor
from typing import List
from scipy.optimize import milp, LinearConstraint

def create_matrix(length:int, true_indicies: List[List[int]]):
    mat: List[List[int]] = []
    for _ in range(length): mat.append([])
    for col in true_indicies:
        for row in range(length):
            mat[row].append(1 if row in col else 0)

    return mat



part1_total = 0
part2_total = 0

# parse the file
with open('Day10/input.txt','r') as f:
    for line in f:
        # parse line

        # yes, yes, array parsing, I like it but it is hard to understand

        # split by white space, and take only the center of each, this removes parens, square brackets, curly braces
        entries = [x[1:-1] for x in line.split()]

        # take the first entry and decode a binary number where '#' means 1. 2 to the power of the position
        lights = sum([2**i*(x=='#') for i,x in enumerate(entries[0])])
        # get rid of the lights and joltage. For each wiring diagram, take 2 to the power of each index and sum them
        buttons1 = [sum([2**int(y) for y in x.split(',')]) for x in entries[1:-1]]
        # get rid of the lights and joltage, and create a matrix where each row is a diagram and 1s are the indicies specified
        buttons2 = create_matrix(len(entries[0]),[[int(y) for y in x.split(',')] for x in entries[1:-1]])
        # create this as a list
        joltage = [int(x) for x in entries[-1].split(',')]

        
        # surely this loop will break early
        try:
            for b in range(1,len(buttons1)):
                for c in combinations(buttons1,b):
                    if reduce(xor,c,0)==lights:
                        raise StopIteration
        except StopIteration:
            pass
        part1_total += b # type: ignore

        # part 2 will use breadth first search
        # nevermind BFS is too slow with such large input numbers (literally 30 joltage are too large)
        # amazingly, this appears to be a very well disguised linear programming problem
        
        # all wiring diagrams create the constraints matrix
        # that is buttons2 is A and joltage is b
        # non-negative x1,..., yep

        # not all best solutions are integers, so I am using the Mixed Integer Linear Program solver
        res = milp([1]*(len(entries)-2),constraints=LinearConstraint(buttons2,joltage,joltage),integrality=1)
        part2_total += res.fun
        



print('Part 1:',part1_total)
print('Part 2:',part2_total)


