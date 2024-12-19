# The stones are completely independent of one another, at least in part 1
# I expect part 2 will ask about a larger number of iterations
# I was right



# count the digits in a number using log 10
from math import floor, log
from functools import cache

def digits(n):
    return floor(log(n,10))+1


# counts how many stones after iterations with a stone of the given value
# this function is predictable, caching results
@cache
def count_stones(iterations,stone_value):
    if iterations == 0:
        return 1
    
    if stone_value == 0:
        return count_stones(iterations-1,1)
    
    d = digits(stone_value)
    if d % 2 == 0:
        return count_stones(iterations-1,stone_value // 10**(d // 2)) + count_stones(iterations-1,stone_value % 10**(d // 2))
    
    # else
    return count_stones(iterations-1,stone_value*2024)



with open('Day11/input.txt') as f:
    starts = [int(x) for x in f.read().split(' ')]

total_count = 0
for stone in starts:
    total_count += count_stones(25,stone)

print('Part 1:',total_count)

total_count = 0
for stone in starts:
    total_count += count_stones(75,stone)

print('Part 2:',total_count)
