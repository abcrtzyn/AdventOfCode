
def is_valid_triangle(a: int,b: int,c: int):
    return a-b-c < 0 and b-c-a < 0 and c-a-b < 0

count = 0
with open('Day03/input.txt') as f:
    i = 0
    for line in f.readlines():
        line = [int(x) for x in line.strip().split()]
        if is_valid_triangle(line[0],line[1],line[2]):
             # possible triangles
             count += 1


print('Part 1:', count)
