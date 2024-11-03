from math import gcd


key =   '10001001100000001'
inkey = '01111111001101110'

# the reverse invert of state0 and state1 are themselves
# state0 = key + '0' + inkey
# state1 = key + '1' + inkey


def generate(length: int,s:str):
    sub_length = (length-1)/2
    #print(sub_length)
    if sub_length <= 17:
        g1 = key
        g2 = inkey
    else:
        g1 = generate(int(sub_length)+1,'0')
        g2 = generate(int(sub_length)+1,'1')

    for c in g1:
        yield c
    yield s
    for c in g2:
        yield c
    

def checksum(sg,l,iterations):
    if iterations == 1:
        g = sg
    else:
        g = checksum(sg,l*2,iterations-1)

    for _ in range(l):
        a = next(g)
        b = next(g)
        
        yield '1' if a == b else '0'
    
    
    #if gcd(l,2) == 2:
        

#length = 272
#iterations = 4
length = 35651584
iterations = 21

g = generate(length,'0')

print(''.join(checksum(g,17,iterations)))
