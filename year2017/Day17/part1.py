
# skip = 3
skip = 345


l = [0]

p = 0

for i in range(1,2018):
    p += skip
    p %= (len(l))
    p += 1
    l.insert(p,i)
    # print(l)

print(l[l.index(0)+1])
