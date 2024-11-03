import re

rule = re.compile('p=<(-?\\d+),(-?\\d+),(-?\\d+)>, v=<(-?\\d+),(-?\\d+),(-?\\d+)>, a=<(-?\\d+),(-?\\d+),(-?\\d+)>')


def distance(t:int,px:int,py:int,pz:int,vx:int,vy:int,vz:int,ax:int,ay:int,az:int):
    return abs(px+vx*t+ax*(t*(t+1))/2)+abs(py+vy*t+ay*(t*(t+1))/2)+abs(pz+vz*t+az*(t*(t+1))/2)

minimum = 100000000000
minimum_at = -1

with open('Day20/input.txt') as f:
    for i,line in enumerate(f.readlines()):
        mat = rule.match(line)
        if mat is None:
            print('could not match line')
            exit(1)
        d = distance(1000,*[int(e) for e in mat.groups()])
        if d < minimum:
            minimum = d
            minimum_at = i

print(minimum_at)
        
