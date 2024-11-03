from typing import List
import re

# i could not get part2 by myself, the solution requires using a cache table to remember previous solutions
DP = {}

def countPossibles(line: str, numbers: List[int]) -> int:
    #print(line, numbers)

    key = (len(line),len(numbers))
    if key in DP:
        return DP[key]
    
    # completely different approach than part 1
    # place the numbers and see if they fit
    
    if len(numbers) == 0:
        # print('no more numbers')
        if line.count('#') == 0:
            # print('made it to the end')
            return 1
        else:
            # print('did not make it to the end')
            return 0


    n = numbers[0]
    # place it in the first spot possible
    pat = re.compile(f'^[?.]*?([?#]{{{n}}})([.?]|$)')

    i = 0
    pos = 0;

    while line[i:].count('#')+line[i:].count('?') >= sum(numbers) and i < len(line):
        
        # print(line[i:],numbers)
        m = pat.match(line[i:])
        if m == None:
            # print('no more positions found')
            # no positions found
            break
        else:
            # print(m.group(0), m.group(1))
            # try the next number starting past the end of this one
            pos += countPossibles(line[i+m.end():],numbers[1:])
            if line[i+m.start(1)] == '#':
                # this is forced match, no more are allowed
                break

            # new start for the next iteration
            i += m.start(1) + 1

    # print('not enough space')
    DP[key] = pos
    return pos




with open('Day12/input.txt') as f:
    count = 0
    for i,line in enumerate(f.readlines()):
        #print(i)
        chars, numbers  = line.split()
        
        a=list()
        a.append(chars)
        chars = '?'.join(5*a)
        numbers = 5*[int(x) for x in numbers.split(',')]
        DP = {}
        count += countPossibles(chars, numbers)

        
    print(count)

    