from typing import List

def is_valid_triangle(a: int,b: int,c: int):
    return a-b-c < 0 and b-c-a < 0 and c-a-b < 0


count = 0
with open('Day03/input.txt') as f:
    i = 0
    t1: List[int] = []
    t2: List[int] = []
    t3: List[int] = []
    for line in f.readlines():
        line = [int(x) for x in line.strip().split()]
        t1.append(line[0])
        t2.append(line[1])
        t3.append(line[2])

        i += 1
        if i % 3 == 0:
           # print(t1,t2,t3)
            if is_valid_triangle(t1[0],t1[1],t1[2]):
                count += 1
            if is_valid_triangle(t2[0],t2[1],t2[2]):
                count += 1
            if is_valid_triangle(t3[0],t3[1],t3[2]):
                count += 1
            t1 = []
            t2 = []
            t3 = []


print('Part 2:',count)
