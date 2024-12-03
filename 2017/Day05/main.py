

def solve(numbers,part2: bool):
    limit = len(numbers)
    i = 0
    jump_count = 0

    while 0 <= i < limit:
        jump = numbers[i]
        # adjust numbers
        if part2 and jump >= 3:
            numbers[i] -= 1
        else:
            numbers[i] += 1
        i += jump
        jump_count += 1
    
    return jump_count


# each line is a number, make a list
numbers = []
with open('Day05/input.txt') as f:
    for x in f:
        numbers.append(int(x.strip()))


print('Part 1:',solve(numbers.copy(),False))
print('Part 2:',solve(numbers.copy(),True))
