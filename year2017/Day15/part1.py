




def generator(seed, start):
    value = start
    while True:
        value = (seed * value) % 2147483647
        yield value


pairs_count = 0

genA = generator(16807,783)
genB = generator(48271,325)

for _ in range(40000000):
    if (next(genA)&0b1111111111111111) == (next(genB)&0b1111111111111111):
        pairs_count += 1

print(pairs_count)
