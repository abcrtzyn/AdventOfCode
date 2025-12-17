from typing import Any, Generator

with open('Day16/input.txt', 'r') as f:
    key = f.readline().strip()

# inkey in the inverse and reverse of the key
inkey = ''.join(['0' if x=='1' else '1' for x in key][::-1])


# the reverse invert of state0 and state1 are themselves
# state0 = key + '0' + inkey
# state1 = key + '1' + inkey

# generates the dragon curve string from the global key and inkey.
def generate(length: int,s:str) -> Generator[str, Any, None]:
    sub_length = (length-1)/2
    #print(sub_length)
    if sub_length <= 17:
        g1 = key
        g2 = inkey
    else:
        g1 = generate(int(sub_length)+1,'0')
        g2 = generate(int(sub_length)+1,'1')

    # spit it out a charecter at a time
    for c in g1:
        yield c
    yield s
    for c in g2:
        yield c
    

def checksum(sg: Generator[str, Any, None],l: int,iterations: int):
    if iterations == 1:
        g = sg
    else:
        g = checksum(sg,l*2,iterations-1)

    for _ in range(l):
        a = next(g)
        b = next(g)
        
        yield '1' if a == b else '0'
        

# the number of iterations of the checksum is determined by how many times the length can be divided by 2
# It seems there is no way to do this other than a loop and it isn't input dependent so it is hard coded here.
# the length of the checksum is the result after dividing by 2 a lot.

g = generate(272,'0')
print('Part 1:', ''.join(checksum(g,17,4))) # 4 iterations, length 17

# part 2 is definitely slow, but good enough for me.
g = generate(35651584,'0')
print('Part 2:', ''.join(checksum(g,17,21))) # 21 iterations, length 17
