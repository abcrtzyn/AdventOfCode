total = 0
with open('Day08/input.txt') as f:
    for line in f.readlines():
        print(line.strip())
        # first quote and last quote always count
        stotal = 2
        
        l = iter(line.strip())
        try:
            while True:
                c = next(l)
                match c:
                    case '\\':
                        stotal += 1
                    case '"':
                        stotal += 1
                    case _:
                        stotal += 0
                

        except StopIteration:
            pass
        
        total += stotal

print(total)