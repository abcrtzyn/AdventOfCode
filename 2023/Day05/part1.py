
with open('Day05/test_input.txt') as f:
    seeds = [int(x) for x in f.readline()[7:].split()]
    lines = [x[:-1] for x in f.readlines()][:-1]

    maps = list()
    skip = False
    for line in lines:
        if (line == ''):
            maps.append(list())
            skip = True
        elif (skip):
            skip = False;
            continue
        else:
            maps[-1].append([int(x) for x in line.split()])
    
    
    for m in maps:
        seedsNew = [];
        for seed in seeds:
            # print(seed)
            for line in m:
                # print(line)
                if seed >= line[1] and seed < line[1] + line[2]:
                    #print(seed,'in range',seed+line[0]-line[1])
                    seedsNew.append(seed + line[0] - line[1])
                    break;
            else:
                seedsNew.append(seed)
        seeds = seedsNew;
    print(min(seedsNew))
