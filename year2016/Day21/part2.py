word = ['f','b','g','d','c','e','a','h']
# word = ['f','d','h','b','c','g','e','a']
# word = ['d','e','c','a','b']

import re
from typing import List

swap_pos_rule = re.compile('swap position (\\d) with position (\\d)')
swap_ltr_rule = re.compile('swap letter (\\w) with letter (\\w)')
rotate_dir_rule = re.compile('rotate (left|right) (\\d) steps?')
rotate_bas_rule = re.compile('rotate based on position of letter (\\w)')
reverse_rule = re.compile('reverse positions (\\d) through (\\d)')
move_rule = re.compile('move position (\\d) to position (\\d)')

# invariant in reverse
def swap_pos(word: List[str], mat: re.Match[str]):
    x = int(mat.group(1))
    y = int(mat.group(2))
    
    temp = word[x]
    word[x] = word[y]
    word[y] = temp
    
    return word

# invariant in reverse
def swap_ltr(word: List[str], mat: re.Match[str]):
    x = mat.group(1)
    y = mat.group(2)
    i = word.index(x)
    j = word.index(y)
    
    temp = word[i]
    word[i] = word[j]
    word[j] = temp
    
    return word

# reverse change direction
def rotate_dir(word: List[str], mat: re.Match[str]):
    dire = mat.group(1) == 'left'
    steps = int(mat.group(2))

    if dire:
        # rotate right - reverse left
        newword = word[-steps:] + word[0:-steps]
    else:
        # rotate left - reverse right
        newword = word[steps:] + word[:steps]

    return newword

# hard reverse
def rotate_bas(word: List[str], mat: re.Match[str]):

    steps = [1,1,6,2,7,3,0,4][word.index(mat.group(1))]
    
    newword = word[steps:] + word[:steps]
    
    return newword

# invariant to reverse
def reverse(word: List[str], mat: re.Match[str]):
    x = int(mat.group(1))
    y = int(mat.group(2))

    word[x:y+1] = reversed(word[x:y+1])

    return word

# !!!!!!!!!!!!!!!!!!!!!!!!!!
def move(word: List[str], mat: re.Match[str]):
    y = int(mat.group(1))
    x = int(mat.group(2))

    l = word.pop(x)
    word.insert(y,l)
    
    return word

rules = [swap_pos_rule, swap_ltr_rule, rotate_dir_rule, rotate_bas_rule, reverse_rule, move_rule]
handlers = [swap_pos, swap_ltr, rotate_dir, rotate_bas, reverse, move]

with open('Day21/input.txt') as f:
    for line in reversed(f.readlines()):
        for rule, handle in zip(rules,handlers):
            mat = rule.match(line)
            if mat is not None:
                word = handle(word,mat)
                break
        #print(line.strip(),''.join(word))

print(''.join(word))
