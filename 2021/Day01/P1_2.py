increasingCount = 0
with open("input.txt", "r") as f:
    n = int(f.readline())
    m = int(f.readline())
    o = int(f.readline())
    sum = n + m + o
    while (l := f.readline()) != "":
        p = int(l)
        newSum = m + o + p
        if newSum > sum:
            increasingCount += 1
        n = m
        m = o
        o = p
        sum = newSum

print(increasingCount)