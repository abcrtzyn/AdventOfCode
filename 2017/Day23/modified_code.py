from cmath import sqrt
from math import ceil


a = 1

b = 84
c = 84


if a == 1:
    b *= 100
    b += 100000
    c = b + 17000


composite_count = 0

while b <= c:
    for i in range(2,int(b**0.5)+1): # type: ignore
        if b % i == 0:
            print(f'{b} is {i}*{int(b/i)}')
            composite_count += 1
            break
    else:
        print(f'{b} is prime')
    


    b += 17

print(composite_count)
