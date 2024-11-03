import itertools


hails = []
with open('Day24/input.txt') as f:
    for line in f.readlines():
        p,v = line.strip().split('@')
        p = tuple([int(x) for x in p.split(',')])
        v = tuple([int(x) for x in v.split(',')])
        hails.append((p,v))

#print(hails)

cross_count = 0

for ((apx,apy,apz),(avx,avy,avz)),((bpx,bpy,pbz),(bvx,bvy,bvz)) in itertools.combinations(hails,2):
    # each hailstone is a line in point slope. The equations cross when the difference of the two is 0
    # (bvy/bvx (x-bpx)+bpy) - (avy/avx) (x-apx)+apy) = 0
    # implemented is solved for x
    if (avy/avx-bvy/bvx) != 0:
        cross_x = (avy*apx/avx-bvy*bpx/bvx+bpy-apy)/(avy/avx-bvy/bvx)
        #print(cross_x)
        cross_y = (avy/avx)*(cross_x-apx)+apy
        # a few other requirements
        # the crossing must happen in the direction both hailstones are moving
        # none of the lines are vertial or horizontal, only checking x direction is suffiecient
        if not ((cross_x > apx) == (avx > 0) and (cross_x > bpx) == (bvx > 0)):
            # the crossing happens in the past
            #print('past crossing')
            continue
        # the crossing must happen within the test area
        if not (200000000000000 <= cross_x <= 400000000000000 and 200000000000000 <= cross_y <= 400000000000000):
            #print('not in test zone')
            continue

        cross_count += 1
    else:
        print('lines are parallel')

print(cross_count)