count = 0
with open('Day03/input.txt') as f:
    i = 0
    t1 = []
    t2 = []
    t3 = []
    for line in f.readlines():
        line = [int(x) for x in line.strip().split()]
        t1.append(line[0])
        t2.append(line[1])
        t3.append(line[2])

        i += 1
        if i % 3 == 0:
           # print(t1,t2,t3)
            if (t1[0]-t1[1]-t1[2] < 0) and (t1[1]-t1[2]-t1[0] < 0) and (t1[2]-t1[0]-t1[1] < 0):
                count += 1
            if (t2[0]-t2[1]-t2[2] < 0) and (t2[1]-t2[2]-t2[0] < 0) and (t2[2]-t2[0]-t2[1] < 0):
                count += 1
            if (t3[0]-t3[1]-t3[2] < 0) and (t3[1]-t3[2]-t3[0] < 0) and (t3[2]-t3[0]-t3[1] < 0):
                count += 1
            t1 = []
            t2 = []
            t3 = []
        
        #if i > 10:
        #    break
        
print(count)    