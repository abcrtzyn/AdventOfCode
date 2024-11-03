




def generator(seed, start,mult):
    value = start
    while True:
        value = (seed * value) % 2147483647
        if value % mult == 0:
            yield value


pairs_count = 0

genA = generator(16807,783,4)
genB = generator(48271,325,8)

for _ in range(5000000):
    if (next(genA)&0b1111111111111111) == (next(genB)&0b1111111111111111):
        pairs_count += 1

print(pairs_count)
