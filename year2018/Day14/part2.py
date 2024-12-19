from typing import List


recipes: List[int] = [3,7]

elf1 = 0
elf2 = 1

SEARCH = [6,3,7,0,6,1]


while True:
    # print(recipes, elf1, elf2)
    new = recipes[elf1] + recipes[elf2]
    if new >= 10:
        recipes.append(int(new/10))
        if recipes[-6:] == SEARCH:
            print(len(recipes)-6)
            exit(0)

    recipes.append(new%10)
    if recipes[-6:] == SEARCH:
        print(len(recipes)-6)
        exit(0)
        
    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

print(recipes[INDEX:INDEX+10])
