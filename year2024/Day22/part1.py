
# does one single iteration
def iterate(seed: int):
    seed = (seed ^ (seed << 6)) & 0xFFFFFF
    seed = (seed ^ (seed >> 5))
    seed = (seed ^ (seed << 11)) & 0xFFFFFF
    return seed


total = 0


with open('Day22/test_input2.txt') as f:
    for line in f:
        value = int(line)
        for _ in range(2000):
            value = iterate(value)
        
        total += value


print('Part 1:',total)
