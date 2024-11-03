maps = {10: 'eqrr', 
         9: 'eqri', 
         0: 'eqir', 
         3: 'gtri',
        13: 'gtrr',
         5: 'gtir',
        12: 'setr',
         7: 'banr',
        11: 'bani',
        15: 'seti',
         2: 'addr',
        14: 'addi',
         6: 'mulr',
         1: 'borr',
         8: 'bori',
         4: 'muli'
}


with open('Day16/programbin.txt') as f:
    with open('Day16/program.txt','w') as g:
        for line in f:
            txt = line.split(' ')
            txt[0] = maps[int(txt[0])]
            g.write(' '.join(txt))
