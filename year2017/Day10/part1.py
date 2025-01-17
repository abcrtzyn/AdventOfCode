
ring = list(range(256))

skip = 0

rotations = 0

with open('Day10/input.txt') as f:
    for line in f.readlines():
        op = int(line)
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


# put the ring back
# print(rotations, rotations % len(ring))
rotations = rotations % len(ring)
operand = ring[0:rotations]
ring = ring[rotations:]
ring.extend(operand)
print(ring)
