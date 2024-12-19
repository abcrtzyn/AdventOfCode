


# for elves in range(1,129):
#     # print(list(range(1,elves+1)))

elves = 300

circle = list(range(1,elves+1))
while len(circle) > 1:
    # the first elf in the list steals presents from the elf halfway in the list
    circle.pop(int(len(circle)/2))
    circle.append(circle.pop(0))
    #print(circle)
print(elves,',',circle[0])
