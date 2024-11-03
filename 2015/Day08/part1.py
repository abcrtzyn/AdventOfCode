total = 0
with open('Day08/input.txt') as f:
    for line in f.readlines():
        #print(line.strip())
        # first quote and last quote always count
        ltotal = 2
        l = iter(line.strip()[1:-1])
        try:
            while True:
                c = next(l)
                if c == '\\':
                    # escape chars
                    c = next(l)
                    if c == 'x':
                        c = next(l)
                        c = next(l)
                        ltotal += 3
                        continue
                    elif c == '\\':
                        ltotal += 1
                        continue
                    elif c == '"':
                        ltotal += 1
                        continue
                else:
                    pass
        except StopIteration:
            pass
        total += ltotal

print(total)