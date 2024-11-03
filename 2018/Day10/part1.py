# the first thing to see is that all the numbers are in the 10000s
# and are approximately 10750x the velocity

# lets bring the numbers down by 10600*v
# then find the most compact time
import re
line_rule = re.compile("position=<([ -]\\d+), ([ -]\\d+)> velocity=<([ -]\\d+), ([ -]\\d+)>")


points = []

with open('Day10/input.txt') as f:
    for line in f:
        mat = line_rule.match(line)
        if mat == None:
            exit(1)
        
        px,py,vx,vy = [int(x) for x in mat.groups()]

        points.append((px+10600*vx,py+10600*vy,vx,vy))


def iterate():
    min_x = 10000000
    max_x = -10000000
    min_y = 10000000
    max_y = -10000000
    
    for i in range(len(points)):
        px,py,vx,vy = points[i]
        npx = px+vx
        npy = py+vy
        points[i] = (npx,npy,vx,vy)
        if npx < min_x:
            min_x = npx
        elif npx > max_x:
            max_x = npx
        if npy < min_y:
            min_y = npy
        elif npy > max_y:
            max_y = npy
    
    return (max_x-min_x)*(max_y-min_y)

def uniterate():
    min_x = 10000000
    max_x = -10000000
    min_y = 10000000
    max_y = -10000000
    
    for i in range(len(points)):
        px,py,vx,vy = points[i]
        npx = px-vx
        npy = py-vy
        points[i] = (npx,npy,vx,vy)
        if npx < min_x:
            min_x = npx
        elif npx > max_x:
            max_x = npx
        if npy < min_y:
            min_y = npy
        elif npy > max_y:
            max_y = npy
    
    return (max_x-min_x)*(max_y-min_y)


iterations = 10600
entropy = 1000000000
while True:
    print(entropy)
    n_entropy = iterate()
    iterations += 1
    if n_entropy > entropy:
        print('we got one')
        print(iterations-1)
        print(points[0:50])
        exit(0)
    entropy = n_entropy
