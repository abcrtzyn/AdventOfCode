# hard limits, in x, 1/2(sqrt(1+8left)-1) <= v <= right
#              in y, down <= v <= -down-1 
from math import floor, ceil, sqrt
import numpy as np

def p_x(t,v_x):
    maxP_x = (v_x^2+v_x)/2
    if t > v_x:
        return maxP_x
    else:
        return t*v_x - (t * (t-1))/2

leftLimit = 265
rightLimit = 287
downLimit = -103
upLimit = -58

v_xLowLimit = ceil((1/2)*(sqrt(1+8*leftLimit)-1))
v_xHighLimit = rightLimit
v_yLowLimit = downLimit
v_yHighLimit = -downLimit-1

print(f'{v_xLowLimit} <= v_x <= {v_xHighLimit}')
print(f'{v_yLowLimit} <= v_y <= {v_yHighLimit}')


#calculatedHeights = np.zeros((1, v_yHighLimit-v_yLowLimit+1), dtype=np.int16)
#calculatedHeightsValidAfter = np.zeros((1, v_yHighLimit-v_yLowLimit+1), dtype=np.int16)
def maxHeight(v_y):
    if v_y > 0: 
        return floor(1/2*(v_y**2 + v_y + 1/4))
    else:
        return 0

def heightValidAfter(v_y):
    if v_y > 0:
        return v_y
    else:
        return 0

def inTarget(x,y):
    return leftLimit <= x <= rightLimit and downLimit <= y <= upLimit

#hitTarget = np.zeros((v_xHighLimit-v_xLowLimit+1, v_yHighLimit-v_yLowLimit+1), dtype=np.bool8)
count = 0
for j in range(v_yHighLimit,v_yLowLimit-1,-1):
    for i in range(v_xLowLimit, v_xHighLimit+1):
        v_x = i
        v_y = j
        x = 0
        y = 0
        t = 0
        while x <= rightLimit and y >= downLimit:
            x += v_x
            y += v_y
            if v_x > 0:    
                v_x -= 1
            v_y -= 1
            if inTarget(x,y):
                count += 1
                break
print(count)
                

#actualHeights = np.zeros((v_xHighLimit-v_xLowLimit+1, v_yHighLimit-v_yLowLimit+1), dtype=np.int16)


