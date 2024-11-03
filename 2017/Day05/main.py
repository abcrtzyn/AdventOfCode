PART2 = True


# each line is a number, make a list

numbers = []

with open('Day05/input.txt') as f:
    for x in f.readlines():
        numbers.append(int(x.strip()))

#print(numbers)


limit = len(numbers)
i = 0
jump_count = 0

while 0 <= i < limit:
    jump = numbers[i]
    if PART2 and jump >= 3:
        numbers[i] -= 1
    else:
        numbers[i] += 1
    i += jump
    jump_count += 1

for x in numbers[0:500]:
    print(x)

print('steps:', jump_count)
