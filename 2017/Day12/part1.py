import re

rule = re.compile('(\\d+) <-> ([0-9, ]+)')


groups = []

with open('Day12/input.txt') as f:
    lines = f.readlines()
    
    all_el = set(range(2000))

    while len(all_el) > 0:
        start = min(all_el)
        
        connected = set()
        connected.add(start)
        stack = [start]
        while len(stack) > 0:
            element = stack.pop()
            line = lines[element]
            # parse line
            mat = rule.match(line)
            if mat is None:
                print(f'could not match "{line}"')
                exit(1)
            if int(mat.group(1)) != element:
                print(f'line {element} has {mat.group(1)}')
                exit(1)
            pipes = [int(x) for x in mat.group(2).split(', ')]
            
            for con in pipes:
                if con in connected:
                    continue
                connected.add(con)
                stack.append(con)
            # print(stack)
        
        # found all connections
        groups.append(connected)
        all_el = all_el.difference(connected)
        

print(len(groups))
print([len(x) for x in groups])
print(len(groups[0]))
