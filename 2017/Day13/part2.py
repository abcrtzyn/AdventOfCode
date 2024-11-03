



import re
rule = re.compile('(?P<layer>\\d+): (?P<depth>\\d+)')

# for each line
# (t + layer) % (2(depth)-2) != 0
# parse each line first
with open('Day13/input.txt') as f:
    lines = [rule.match(x).groups() for x in f.readlines()] # type: ignore
    lines = [(int(x[0]),2*int(x[1])-2) for x in lines]

# print(lines)
# exit(0)

t = 0

while True:
    if t % 220000000 == 0:
        print(t)
        #print(lines)
        #exit(0)
    try:
        for l in lines:
            if (t + l[0]) % (l[1]) == 0:
                #print(l[0])
                # increment t and start over
                t += 1
                raise Exception()
    except Exception:
        continue
    break


print(t)
