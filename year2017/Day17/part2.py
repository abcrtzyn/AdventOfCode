# we no longer can simulate the buffer, we must keep track of zero and the value after 0

with open('Day17/input.txt') as f:
    skip = int(f.read())


pointer = 0
zero_pos = 0
number_after = None



for i in range(1,50000001):
    pointer += skip
    pointer %= i
    pointer += 1
    # insert
    if pointer <= zero_pos:
        zero_pos += 1
    elif pointer == zero_pos + 1:
        # inserting a new number after 0
        number_after = i
    # if pointer is larger, doesn't matter

print('Part 2:',number_after)
