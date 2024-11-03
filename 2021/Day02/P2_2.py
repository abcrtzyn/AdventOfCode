import re

depth = 0
distance = 0
aim = 0

m = re.compile("(?P<dir>forward|down|up) (?P<num>\\d+)")

with open("input.txt") as f:
    for line in f.readlines():
        matchObject = m.match(line)
        direction = matchObject.group(1)
        number = int(matchObject.group(2))
        if(direction == "forward"):
            distance += number
            depth += aim * number
        elif (direction == "down"):
            aim += number
        elif (direction == "up"):
            aim -= number

print(depth * distance)
