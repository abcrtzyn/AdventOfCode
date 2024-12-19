

with open('Day01/input.txt') as f:
    l = [int(line) for line in f]

a = len(l)

s = set()
s.add(0)

c = 0
i = 0
while True:
    c += l[i%a]
    if c in s:
        print(c)
        exit(0)
    s.add(c)
    i += 1
