with open('input.txt') as f:
    easyDigitsTotal = 0
    for line in f:
        combos, output = tuple([l.strip() for l in line.strip().split('|')])
        digits = output.split()
        for d in digits:
            if len(d) == 2 or len(d) == 3 or len(d) == 4 or len(d) == 7:
                easyDigitsTotal += 1
    print(easyDigitsTotal)