# because the expressions are evaulated from left to right
# working backward is the way to go, backtracking
from typing import List


# returns true if the value can be made using the numbers
def valid(value: int, numbers: List[int], part2: bool):
    
    if len(numbers) == 1:
        return value == numbers[-1]
    
    last = numbers.pop()
    
    if value % last == 0:
        if valid(value // last, numbers, part2):
            # multiplication works
            numbers.append(last)
            return True
    
    if part2:
        valuestr = str(value)
        laststr = str(last)
        # if the last part of value is the same as last, try concatenation
        if valuestr.endswith(laststr):
            if len(valuestr) == len(laststr):
                # creates an empty string, never can happen in the middle of a list
                pass
            elif valid(int(valuestr[:-len(laststr)]),numbers,part2):
                # concatenation works
                numbers.append(last)
                return True
            

    if value - last >= 0:
        if valid(value - last, numbers, part2):
            # addition works
            numbers.append(last)
            return True
    
    numbers.append(last)
    return False

part1total = 0
part2total = 0

with open('Day07/input.txt') as f:
    for line in f:
        n, l = line.split(':')
        n = int(n)
        l = [int(x) for x in l.strip().split(' ')]
        
        if valid(n,l,False):
            part1total += n
            part2total += n
        elif valid(n,l,True):
            part2total += n
        

print('Part 1:', part1total)
print('Part 2:', part2total)
