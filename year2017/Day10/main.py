import functools
import itertools
from typing import List, Literal, overload


@overload
def knothash(s: bytes, part1: Literal[False]) -> List[int]: ...
@overload
def knothash(s: bytes) -> bytes: ...

@overload
def knothash(s: bytes, part1: Literal[True]) -> bytes: ...

def knothash(s: bytes, part1: bool = False):
    reverses = list(s + b'\x11\x1f\x49\x2f\x17' if not part1 else s)
    ring = list(range(256))
    skip = 0
    rotations = 0

    for _ in range(64 if not part1 else 1):
        for op in reverses:
            rotations -= op
            operand = reversed(ring[0:op])
            ring = ring[op:]
            ring.extend(operand)
            #print('op',ring)

            # skip
            if skip > 0:
                rotations -= skip
                operand = ring[0:skip]
                ring = ring[skip:]
                ring.extend(operand)
                #print('skip',ring)

            skip += 1
            skip %= 256

    # put the ring back
    # print(rotations, rotations % len(ring))
    rotations = rotations % len(ring)
    operand = ring[0:rotations]
    ring = ring[rotations:]
    ring.extend(operand)

    if part1:
        return ring
    
    return bytes([functools.reduce(int.__xor__,batch) for batch in itertools.batched(ring,16)])


if __name__ == "__main__":
        
    with open('Day10/input.txt') as f:
        b = bytes(int(x) for x in f.readline().split(','))
        ring = knothash(b,True)

    print('Part 1:',ring[0] * ring[1])


    with open('Day10/input.txt','rb') as f:
        b = f.readline().strip()
        print('Part 2:',knothash(b).hex())
