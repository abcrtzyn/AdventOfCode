
def hash(s: str):
    acc1 = 0
    for c in s:
        acc1 += ord(c)
        acc1 *= 17
        acc1 = acc1 % 256
    return acc1

acc = 0
with open('Day15/input.txt') as f:
    for l in f.readline().strip().split(','):
        acc += hash(l)

print(acc)