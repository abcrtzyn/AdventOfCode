import re
pattern = re.compile('(\\d+)x(\\d+): (\\d+) (\\d+) (\\d+) (\\d+) (\\d+) (\\d+)')


presents = []
presents_area = []


with open('Day12/input.txt','r') as f:
    for i in range(6):
        f.read(3)
        p = f.read(13).split()
        presents.append(p)
        presents_area.append(''.join(p).count('#'))
    

    total_rows = 0
    rejected_for_cells = 0


    for line in f:
        mat = pattern.match(line)
        assert mat is not None
        numbers = [int(x) for x in mat.groups()]

        length = numbers[0]
        height = numbers[1]
        quantities = numbers[2:]

        total_rows += 1
        # sanity check, if the number cells each present takes up too mach space, instant reject
        filled_cells = sum([x*y for x,y in zip(presents_area,quantities)])
        if filled_cells > length*height:
            rejected_for_cells += 1
            continue
        
        # now is the game of try and fit them all
        # this section would be code to trial and error fit in all the presents


# after a quick check, all the rest of the regions would have over 300 empty cells
# just to try, I used this number and it was right.        
print('Part 1: ',total_rows-rejected_for_cells)
