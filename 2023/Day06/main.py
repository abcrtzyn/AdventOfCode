from math import ceil, floor
from functools import reduce
import operator

# solve using a modified quadratic forula
def solve(b, c):
    discrimanant = (b**2-4*c)**0.5
    return floor((b+discrimanant)/2)-ceil((b-discrimanant)/2)+1


# testing data
# p1_bs = [7, 15, 30]
# p1_cs = [9, 40, 200]

p1_bs = [48, 87, 69, 81]
p1_cs = [255, 1288, 1117, 1623]

# testing data
# p2_b = 71530
# p2_c = 940200

p2_b = 48876981
p2_c = 255128811171623

print('Part 1:', reduce(operator.mul,(solve(b,c) for b,c in zip(p1_bs,p1_cs)),1))
print('Part 2:', solve(p2_b,p2_c))
