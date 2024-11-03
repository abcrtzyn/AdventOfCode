# this might be possible with some cancelling rules


current = (0,0,0)
longest = 0

i = 0

with open('Day11/input.txt') as f:
    for d in f.read().strip().split(','):
        match d:
            case 'n':
                current = (current[0]+1,current[1],current[2])
            case 'ne':
                current = (current[0],current[1]+1,current[2])
            case 'se':
                current = (current[0],current[1],current[2]-1)
            case 's':
                current = (current[0]-1,current[1],current[2])
            case 'sw':
                current = (current[0],current[1]-1,current[2])
            case 'nw':
                current = (current[0],current[1],current[2]+1)
            case _:
                print(f'could not match "{d}"')
                exit(1)
        # do simplification rules
        if current[1] > 0 and current[2] > 0:
            # ne nw = n
            x = min(current[1], current[2])
            current = (current[0]+x,current[1]-x,current[2]-x)
        elif current[1] < 0 and current[2] < 0:
            # se sw = s
            x = min(-current[1], -current[2])
            current = (current[0]-x,current[1]+x,current[2]+x)
        
        elif current[0] < 0 and current[1] > 0:
            # s ne = se
            x = min(-current[0], current[1])
            current = (current[0]+x,current[1]-x,current[2]-x)
        elif current[0] > 0 and current[1] < 0:
            # n sw = nw
            x = min(current[0], -current[1])
            current = (current[0]-x,current[1]+x,current[2]+x)
        elif current[0] > 0 and current[2] < 0:
            # n se = ne
            x = min(current[0],-current[2])
            current = (current[0]-x,current[1]+x,current[2]+x)
        elif current[0] < 0 and current[2] > 0:
            # s nw = sw
            x = min(-current[0],current[2])
            current = (current[0]+x,current[1]-x,current[2]-x)

        s = sum(current)
        if s > longest:
            longest = s
        #print(current,end=' ')
        #i += 1
        # if  i > 500:
        #     exit(0)

        

print(f'part1: {s}')
print(f'part2: {longest}')
        
