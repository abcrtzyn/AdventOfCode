
with open('Day17/input.txt') as f:
    skip = int(f.read())


l = [0]

p = 0

for i in range(1,2018):
    p += skip
    p %= (len(l))
    p += 1
    l.insert(p,i)
    # print(l)

print('Part 1:',l[l.index(2017)+1])
