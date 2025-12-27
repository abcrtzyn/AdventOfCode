# this is version 2 of part 2
# I will just sample the grid at (500*n,500*m)
# then with a list of points outside the shape
# remove rectangles

# Im hoping to see less than 3000 rectangles left to 'manually' check

from itertools import combinations
from math import atan2, isclose, pi
from typing import Dict, List, Set, Tuple


threshold = 1

points: List[Tuple[int,int]] = []



with open('Day09/input.txt','r') as f:
    for line in f:
        points.append(tuple([int(x) for x in line.strip().split(',')])) # type: ignore

def area(Ax:int,Ay:int,Bx:int,By:int):
    return (abs(Ax-Bx)+1)*(abs(Ay-By)+1)

# determines if many points are inside the shape by checking the angles going around the shape
# sometimes called the winding algorithm I guess
def is_inside(points_to_check: Set[Tuple[int,int]]):
    winding: Dict[Tuple[int,int],float] = {x:0 for x in points_to_check}
    inside: Set[Tuple[int,int]] = set()
    
    # turtle
    # the previous x,y will start at the last point
    px, py = points[-1]

    # precheck if this point is to be checked
    if (px,py) in winding:
        inside.add((px,py))
        del winding[(px,py)]

    # now the turtle will travel each edge
    for cx,cy in points:
        remove_from_winding: Set[Tuple[int,int]] = set()
        # if this point is to be checked, its inside
        if (cx,cy) in winding:
            inside.add((cx,cy))
            del winding[(cx,cy)]

        for (targetx,targety) in winding:
            # check if the point is on edge of the shape
            if px == cx and targetx == cx and (py < targety < cy or cy < targety < py):
                inside.add((targetx,targety))
                remove_from_winding.add((targetx,targety))
                continue
            if py == cy and targety == cy and (px < targetx < cx or cx < targetx < px):
                inside.add((targetx,targety))
                remove_from_winding.add((targetx,targety))
                continue

            # calculate angle
            # with target as the center, moving from p to c is what angle
            # not dividing by 2 because integers are better
            ax = px-targetx
            ay = py-targety
            bx = cx-targetx
            by = cy-targety
            angle = atan2(ax*by-bx*ay,ax*bx+ay*by)
            winding[(targetx,targety)] += angle

        for rem in remove_from_winding:
            del winding[rem]
        remove_from_winding = set()
        # current point becomes previous
        px = cx
        py = cy
    # check the angle now
    # the points in the input are arranged counter-clockwise, so only positive angles are used
    # negative angles are fine too, I just decided to call it an error
    for point in winding:
        if isclose(winding[point],0,abs_tol=1e-4):
            # if the angle is close to 0, its not in the shape
            pass
        elif isclose(winding[point],2*pi,abs_tol=1e-4):
            # if its close to 2pi, its in the shape
            inside.add(point)
        elif isclose(winding[point],-2*pi,abs_tol=1e-4):
            # if its clos. to -2pi, how?
            print('really shouldn\'t be negative')
            # it could be if the turtle went the opposite dircetion
            exit(90)
        else:
            # if its not close to anything, floating point math is worse than I thought.
            # or an error, which did happen
            print('value not close to anything',winding[point])
            exit(70)
    
    return inside



rectangles = set([(Ax,Ay,Bx,By) for (Ax,Ay),(Bx,By) in combinations(points,2) if area(Ax,Ay,Bx,By)>=threshold])

check: Set[Tuple[int,int]] = set()

# # starting with opposite corners, just becuase its not a huge set of points
# for (Ax,Ay,Bx,By) in rectangles:
#     check.add((Ax,By))
#     check.add((Bx,Ay))

minx = min([p[0] for p in points])
maxx = max([p[0] for p in points])
miny = min([p[1] for p in points])
maxy = max([p[1] for p in points])

# print(minx,maxx,miny,maxy)


# there is a bit of luck when choosing the sample grid
for i in range(minx+100,maxx,200):
    for j in range(miny+100,maxy,200):
        check.add((i,j))


print('checking',len(check),'points')
inside = is_inside(check)
outside = check.difference(inside)
del check


remove_rectangle: Set[Tuple[int,int,int,int]] = set()

for (Ax,Ay,Bx,By) in rectangles:
    # print(Ax,Ay,Bx,By)
    
    # quick check if any point known to be outside is in the middle of the rectangle
    # it turns out that the other rectangle corners is a really good set to test against
    ins = True
    for px,py in outside:
        if (Ax <= px <= Bx or Bx <= px <= Ax) and (Ay <= py <= By or By <= py <= Ay):
            remove_rectangle.add((Ax,Ay,Bx,By))
            ins = False
            break
    if not ins:
        continue

rectangles.difference_update(remove_rectangle)

print(len(rectangles))

for (Ax,Ay,Bx,By) in sorted(rectangles,key=lambda rec: area(*rec),reverse=True):
    print(Ax,Ay,Bx,By)
    
    check = set()
    
    # check set is all corners and edges
    for i in range(min(Ay,By),max(Ay,By)+1):
        check.add((Ax,i))
        check.add((Bx,i))
    for i in range(min(Ax,Bx),max(Ax,Bx)):
        check.add((i,Ay))
        check.add((i,By))

    # could do this, doesn't save much time
    # check.difference_update(inside)

    print('checking',len(check),'points')
    inside_edge = is_inside(check)
    # if all points on the edge are inside the shape, we have found a fully inside rectangle
    if len(check) == len(inside_edge):
        # found it
        print('Part 2:',area(Ax,Ay,Bx,By))
        break



