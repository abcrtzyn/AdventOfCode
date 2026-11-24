# there are of course nice quadratic formulas for
# the axes of the grid
# basically we figure out which is closest, and add the discrepency
# nevermind, I found a way to look at the upper left corner
# 

from math import isqrt


with open('Day03/input.txt') as f:
    INPUT = int(f.read().strip())

# rank is how far out the ring is
rank = (isqrt(INPUT-1)+1)//2
# this is the value of the upper left corner
base = 4*rank**2+1

diff = abs(INPUT - base)
# this is how different the distance is from the rank
offset = abs(abs(-diff+2*rank)-rank) # this is an approximation of a triangle wave, just enough to get it to work
# and the actual answer
distance = rank + offset

print('Part 1:', distance)

