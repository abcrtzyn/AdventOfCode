inst = ''
net = dict()

with open('Day08/input.txt') as f:
    inst = f.readline()[:-1];
    #print(inst);
    f.readline()
    net = {line[0:3]: (line[7:10], line[12:15]) for line in f.readlines()}

for point in ['AAA', 'GCA', 'CMA', 'QNA', 'FTA', 'CBA']:
    steps = 0;
    instSize = len(inst);

    while(point[2]!='Z'):
        if(inst[steps%instSize] == 'L'):
            point = net[point][0]
        else:
            point = net[point][1]
        steps += 1;

    print(point)
    print(steps)
