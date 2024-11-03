import itertools


hails = []
with open('Day24/input.txt') as f:
    for line in f.readlines():
        p,v = line.strip().split('@')
        p = tuple([int(x) for x in p.split(',')])
        v = tuple([int(x) for x in v.split(',')])
        hails.append((p,v))

pass
# facts
# There must exist a projection plane such that all 300 lines intersect at a single point
# the perpendicular line from this point is the only line that works. Then the starting point must be found

# it takes two points to define a line
# a brute force approach to this problem would be
# 1. start with point 1, time step 1; and point 2, time step 2
# these two points define a line.
# look at point 3. If point three line is not intersected, try the next combination

# for the purposes of this algorithm, it is reasonable to believe that the first two hailstones will be hit at t=1 and t=2
# so i will start there

def extrapolate(p,v,t):
    return (p[0]+v[0]*t,p[1]+v[1]*t,p[2]+v[2]*t)

mus = []

def distance_from_line(ap,av,bp,bv):
    # determine the line perpendicular to both lines, return the distance squared
    p1 = ap
    p3 = bp
    
    p13 = (p1[0]-p3[0], p1[1]-p3[1], p1[2]-p3[2])
    p43 = bv
    p21 = av

    if abs(p43[0]) == 0 and abs(p43[1]) == 0 and abs(p43[2]) == 0:
        raise Exception('case not handled',p43)
        return False
    
    if abs(p21[0]) == 0 and abs(p21[1]) == 0 and abs(p21[2]) == 0:
        raise Exception('case not handled',p21)
        return False

    d1343 = p13[0] * p43[0] + p13[1] * p43[1] + p13[2] * p43[2];
    d4321 = p43[0] * p21[0] + p43[1] * p21[1] + p43[2] * p21[2];
    d1321 = p13[0] * p21[0] + p13[1] * p21[1] + p13[2] * p21[2];
    d4343 = p43[0] * p43[0] + p43[1] * p43[1] + p43[2] * p43[2];
    d2121 = p21[0] * p21[0] + p21[1] * p21[1] + p21[2] * p21[2];

    denom = d2121 * d4343 - d4321 * d4321;

    if abs(denom) == 0:
        raise Exception('case not handled',denom)
        return False
    
    numer = d1343 * d4321 - d1321 * d4343;

    #print(numer,denom, numer/denom)
    mua = numer / denom;
    mus.append(mua)

    mub = (d1343 + d4321 * mua) / d4343;
    
    pa = (p1[0]+mua*p21[0],p1[1]+mua*p21[1],p1[2]+mua*p21[2])
    pb = (p3[0]+mub*p43[0],p3[1]+mub*p43[1],p3[2]+mub*p43[2])
    
    return (p1[0]+mua*p21[0]-(p3[0]+mub*p43[0]))**2+(p1[1]+mua*p21[1]-(p3[1]+mub*p43[1]))**2+(p1[2]+mua*p21[2]-(p3[2]+mub*p43[2]))**2
    
    # if pa == pb:#abs(pa[0]-pb[0]) < 0.001 and abs(pa[1]-pb[1]) < 0.001 and abs(pa[2]-pb[2]) < 0.001:
    #     return True
    # #print(pa,pb)
    # if abs(pa[0] - pb[0]) < 0.01 and abs(pa[1] - pb[1]) < 0.01 and abs(pa[2] - pb[2]) < 0.01:
    #     #print(ap,av,bp,bv)
    #     # print(abs(pa[2]-pb[2])<0.001)
    #     print('precision error',pa,pb)
    # return False

# i have learned through visualization what the approximate slope of the line should be
# 1st point, t ~= 399 270 557 617
# 292nd point, t ~= 384 674 566 981
# i should be able to start here, and gradient descent towards the correct answer
# 
ap,av = hails[70]
bp,bv = hails[78]


at = 1043212685754
bt = 62884918104

p1 = extrapolate(ap,av,at)
p2 = extrapolate(bp,bv,bt)
lv = (p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2])

print(p1)
print(p2)
print(lv)
import math
gc = math.gcd(lv[0],lv[1],lv[2])
print(lv[0]/gc,lv[1]/gc,lv[2]/gc)


# 1043212685754 -> (142277931159591, 243096286343884, 316654291848372)
# 62884918104 -> (435395933686941, 339168407573584, 239208398204022)
# velocity is -299, -98, 79
# 0 -> ?

print((p1[0]-p2[0])/980327767650,(p1[1]-p2[1])/980327767650,(p1[2]-p2[2])/980327767650)

print(142277931159591 + 299 * 1043212685754)
print(243096286343884 + 98 * 1043212685754)
print(316654291848372 - 79 * 1043212685754)

print(454198524200037
+ 345331129547776
+ 234240489673806)
# I am now going to try every option within a 100,100 grid centered around this point
# import numpy as np

# grid = np.ones((100,100))


# for i in range(-5,5):
#     for j in range(-5,5):
#         p1 = extrapolate(ap,av,at+i)
#         p2 = extrapolate(bp,bv,bt+j)
#         lv = (p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2])

#         cost = 0
#         for (cp,cv) in hails:
#             if cp == ap or cp == bp:
#                 continue
#             cost += distance_from_line(p1,lv,cp,cv)
#         grid[i+50,j+50] = cost
#         if cost < 1:
#             print(i+50,j+50)

# print(np.min(grid))
#print(grid)

# import matplotlib.pyplot as plt

# plt.matshow(grid)
# plt.show()

p1 = extrapolate(ap,av,at)
p2 = extrapolate(bp,bv,bt)
lv = (p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2])


for (cp,cv) in hails:
    if cp == ap or cp == bp:
        continue
    distance_from_line(p1,lv,cp,cv)