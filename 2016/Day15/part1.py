from math import gcd


i = 0


while True:
    x = 17*7*3*i - 2
    if gcd((x+5),19) == 19 and gcd((x+4),5) == 5 and gcd((x+11),13) == 13 and gcd((x+7),11) == 11:
        print(x)

        a = (2 + x) % 17
        b = (2 + x) % 7
        c = (5 + x) % 19
        d = (4 + x) % 5
        e = (2 + x) % 3
        f = (11 + x) % 13
        g = (7 + x) % 11

        print(a,b,c,d,e,f,g)
        exit(0)



    i += 1
