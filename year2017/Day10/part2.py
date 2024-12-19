import itertools
import functools


with open('Day10/input2.txt','rb') as f:
    b = f.readline().strip()+b'\x11\x1f\x49\x2f\x17'
    reverses = list(b)



ring = list(range(256))

skip = 0

rotations = 0


for _ in range(64):
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

print(ring)

print(bytes([functools.reduce(int.__xor__,batch) for batch in itertools.batched(ring,16)]).hex())
