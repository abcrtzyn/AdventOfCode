#  this is the same as a 2016 day 21
# except that we have to parse chars and not lines


word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
# word = ['a','b','c','d','e']


from io import TextIOWrapper
from typing import List



def swap_pos(word: List[str], x,y):    
    temp = word[x]
    word[x] = word[y]
    word[y] = temp
    
    return word

def swap_ltr(word: List[str],x,y):
    i = word.index(x)
    j = word.index(y)
    
    temp = word[i]
    word[i] = word[j]
    word[j] = temp
    
    return word


def rotate_dir(word: List[str], steps):

    if True:
        # rotate right
        newword = word[-steps:] + word[0:-steps]
    else:
        # rotate left
        newword = word[steps:] + word[:steps]

    return newword

# def rotate_bas(word: List[str], mat: re.Match[str]):
#     steps = word.index(mat.group(1))+1
#     if steps >= 5:
#         steps += 1
#     steps = steps % len(word)

#     newword = word[-steps:] + word[0:-steps]
    
#     return newword


# def reverse(word: List[str], mat: re.Match[str]):
#     x = int(mat.group(1))
#     y = int(mat.group(2))

#     word[x:y+1] = reversed(word[x:y+1])

#     return word

# def move(word: List[str], mat: re.Match[str]):
#     x = int(mat.group(1))
#     y = int(mat.group(2))

#     l = word.pop(x)
#     word.insert(y,l)
    
#     return word



def read_until_char(f:TextIOWrapper, term: str):
    s = ''
    c = f.read(1)
    while c != term and c != '\n':
        s += c
        c = f.read(1)
    return s


with open('Day16/input.txt') as f:
    while True:
        match f.read(1):
            case 's':
                shift = int(read_until_char(f,','))
                word = rotate_dir(word,shift)
            case 'x':
                a = int(read_until_char(f,'/'))
                b = int(read_until_char(f,','))
                word = swap_pos(word,a,b)
            case 'p':
                a = read_until_char(f,'/')
                b = read_until_char(f,',')
                word = swap_ltr(word,a,b)
            case '':
                break
            case _:
                print('no idea what char this is')
                exit(1)
    
print(word)
        
