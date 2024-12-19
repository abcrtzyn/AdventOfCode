
import re
from typing import Dict, List, Tuple

line_rule = re.compile('\\[1518-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2})\\] (Guard #\\d+ begins shift|falls asleep|wakes up)')
guard_start_rule = re.compile('Guard #(\\d+) begins shift')

lines: Dict[int,str]= {}


with open('Day04/input.txt') as f:
    for line in f:
        line_match = line_rule.match(line)
        if line_match is None:
            print(f'did not match "{line}"')
            exit(1)
        
        # map the lines to minutes
        k = 31*24*60*int(line_match.group(1)) + 24*60*int(line_match.group(2)) + 60*int(line_match.group(3)) + int(line_match.group(4))
        v = line_match.group(5)

        lines[k] = v


guard_shifts: Dict[int,List[List[Tuple[int,int,int]]]] = {}

asleep_start = None

for t in sorted(lines.keys()):
    x = lines[t]
    
    match x[0]:
        case 'G':
            # guard start shift
            guard = int(guard_start_rule.match(x).group(1)) # type: ignore
            if guard in guard_shifts:
                guard_shifts[guard].append([])
            else:
                guard_shifts[guard] = [[]]
        case 'f':
            # falls asleep
            if asleep_start is not None:
                print("guard is still asleep")
                exit(10)
            asleep_start = t
        case 'w':
            # wakes up
            if asleep_start is None:
                print('guard already awake')
                exit(10)
            time_asleep = t - asleep_start
            guard_shifts[guard][-1].append((asleep_start%1440,t%1440,time_asleep))
            asleep_start = None

# figure out which one was asleep the longest
asleep_times = {k:sum([sum([y[2] for y in x]) for x in v]) for k,v in guard_shifts.items()}
first_worst_guard = max(asleep_times, key=asleep_times.get) # type: ignore

# figure out when each guard has their worst minute, chooses the first, AOC probably is invariant
guard_worst_minute: Dict[int,Tuple[int,int]] = {}

for guard in guard_shifts:
    minutes = [0] * 60

    for shift in guard_shifts[guard]:
        for sleep in shift:
            for i in range(sleep[0],sleep[1]):
                minutes[i] += 1
    most = max(minutes)
    guard_worst_minute[guard] = (minutes.index(most),most)

guard_worst_minute1 = {k:v[1] for k,v in guard_worst_minute.items()}
second_worst_guard = max(guard_worst_minute1, key=guard_worst_minute1.get) #type: ignore

print(f'part 1: {first_worst_guard * guard_worst_minute[first_worst_guard][0]}')
print(f'part 2: {second_worst_guard * guard_worst_minute[second_worst_guard][0]}')
