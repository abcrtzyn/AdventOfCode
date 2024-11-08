total = 0

with open('Day08/input.txt') as f:
    for line in f.readlines():
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
                        # hex, requires 4 chars to encode 1
                        c = next(l)
                        c = next(l)
                        ltotal += 3
                    elif c == '\\' or c == '"':
                        # " or \, requires 2 chars to encode 1
                        ltotal += 1
                    else:
                        raise Exception('unknown escape sequence')
                
        except StopIteration:
            pass
        total += ltotal

print('Part 1:',total)
