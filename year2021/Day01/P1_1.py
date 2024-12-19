# n: int = 0
increasingCount = 0
with open("input.txt", "r") as f:
    line = f.readline()
    n = int(line)

    while (l := f.readline()) != "":
        m = int(l)
        if m > n:
            increasingCount += 1
        n = m

print(increasingCount)


    
    


