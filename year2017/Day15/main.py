
with open('Day15/input.txt') as f:
    g1_start, g2_start = (int(line.split()[-1]) for line in f)



def generator(seed: int, start: int,mult: int):
    value = start
    while True:
        value = (seed * value) % 2147483647
        if value % mult == 0:
            yield value



genA = generator(16807,g1_start,1)
genB = generator(48271,g2_start,1)

pairs_count = 0

for _ in range(40_000_000):
    if next(genA) & 0b1111111111111111 == next(genB) & 0b1111111111111111:
        pairs_count += 1

print('Part 1:', pairs_count)


genA = generator(16807,g1_start,4)
genB = generator(48271,g2_start,8)

pairs_count = 0

for _ in range(5_000_000):
    if (next(genA) & 0b1111111111111111) == (next(genB) & 0b1111111111111111):
        pairs_count += 1

print('Part 2:', pairs_count)
