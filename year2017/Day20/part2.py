import re

rule = re.compile('p=<(-?\\d+),(-?\\d+),(-?\\d+)>, v=<(-?\\d+),(-?\\d+),(-?\\d+)>, a=<(-?\\d+),(-?\\d+),(-?\\d+)>')


particles = {}
positions = {}


with open('Day20/input.txt') as f:
    for i,line in enumerate(f.readlines()):
        mat = rule.match(line)
        if mat is None:
            print('could not match line')
            exit(1)
        particles[i] = [int(e) for e in mat.groups()]

for _ in range(500):
    # reset collision index
    positions = {}
    remove = []
    for particle,info in particles.items():
        #print(particle,info)
        
        info[3] += info[6]
        info[4] += info[7]
        info[5] += info[8]
        info[0] += info[3]
        info[1] += info[4]
        info[2] += info[5]
        particles[particle] = info
    
        if (info[0],info[1],info[2]) in positions:
            # collision
            #print('collision')
            remove.append(particle)
            k = positions[info[0],info[1],info[2]]
            if k not in remove:
                remove.append(k)
        else:
            positions[(info[0],info[1],info[2])] = particle

    for p in remove:
        del particles[p]


print(len(particles))


        
