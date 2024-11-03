weapons = [('dagger', 8, 4, 0), ('shortsword', 10, 5, 0), ('warhammer', 25, 6, 0), ('longsword', 40, 7, 0), ('greataxe', 74, 8, 0)]
armour = [('none', 0, 0, 0), ('leather', 13, 0, 1), ('chainmail', 31, 0, 2), ('splintmail', 53, 0, 3), ('bandedmail', 75, 0, 4), ('platemail', 102, 0, 5)]
rings = [('none', 0, 0, 0), ('damage1', 25, 1, 0), ('damage2', 50, 2, 0), ('damage3', 100, 3, 0), ('defense1', 20, 0, 1), ('defense2', 40, 0, 2), ('defense3', 80, 0, 3)]

ph = 100

bh = 103
ba = 2
bd = 9

def accumulate_stats(w,a,r1,r2):
    return (w[1]+a[1]+r1[1]+r2[1],w[2]+a[2]+r1[2]+r2[2],w[3]+a[3]+r1[3]+r2[3])

for w in weapons:
    for a in armour:
        for i,r1 in enumerate(rings):
            for r2 in rings[i:]:
                if r2 == r1 and r2 != ('none', 0, 0, 0):
                    continue
                print(w,a,r1,r2)
                c,att,arm = accumulate_stats(w,a,r1,r2)
                plturns = bh/(att-ba)
                if bd-arm == 0:
                    boturns = 10000000000
                else:
                    boturns = ph/(bd-arm)
                print(plturns,boturns)
                # determine
                raise Exception('not implemented')
    exit()