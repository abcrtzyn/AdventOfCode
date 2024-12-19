workflows = {}
parts = []

with open('Day19/input.txt') as f:
    emptyline = False

    for line in f.readlines():
        line = line.strip()
        if line == '':
            emptyline = True
            continue
        if emptyline:
            line = line.strip('{}')
            line = line.split(',')
            attributes = {p[0]: int(p[2:]) for p in line}
            parts.append(attributes)
        else:
            i = line.find('{')
            flow = line[0:i]
            line = line[i+1:-1] # gets rid of the {}
            steps = line.split(',')
            final = steps[-1]
            steps = [step.split(':') for step in steps[:-1]]
            steps = [(step[0][0],step[0][1],int(step[0][2:]),step[1]) for step in steps]
            steps.append(('m','>',0,final)) # unconditional final stage
            workflows[flow] = steps;

#print(parts)
#print(workflows)

score = 0
i = 0
for part in parts:
    #print(part)
    # start with the workflow 'in'
    currentFlow = 'in'
    i = 0
    while True:
        step = workflows[currentFlow][i]
        #print(currentFlow, i, step)
        if step[1] == '>':
            if part[step[0]] > step[2]:
                if step[3] == 'A':
                    # process
                    score += part['x'] + part['m'] + part['a'] + part['s']
                    break
                elif step[3] == 'R':
                    break
                else:
                    currentFlow = step[3]
                    i = 0
            else:
                i += 1
        elif step[1] == '<':
            if part[step[0]] < step[2]:
                if step[3] == 'A':
                    # process
                    score += part['x'] + part['m'] + part['a'] + part['s']
                    break
                elif step[3] == 'R':
                    break
                else:
                    currentFlow = step[3]
                    i = 0
            else:
                i += 1

print(score)