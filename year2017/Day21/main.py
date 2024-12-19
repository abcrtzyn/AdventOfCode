


from typing import Dict, List


def rotate2x2(s:str):
    # 01/  => 30/
    # 34      41
    return s[3] + s[0] + s[2] + s[4] + s[1]

# rotations will be good enough for 2x2

def rotate3x3(s:str):
    # 012/  =>  840/
    # 456/      951/
    # 89X       X62
    return s[8] + s[4] + s[0] + s[3] + s[9] + s[5] + s[1] + s[7] + s[10] + s[6] + s[2]

def flip3x3(s:str):
    # 012/ =>  210/
    # 456/     654/
    # 89X      X98
    return s[2] + s[1] + s[0] + s[3] + s[6] + s[5] + s[4] + s[7] + s[10] + s[9] + s[8]

rules2x2: Dict[str,str] = {}
rules3x3: Dict[str,str] = {}

import re
rule2 = re.compile('([#\\.]{2}/[#\\.]{2}) => ([#\\.]{3}/[#\\.]{3}/[#\\.]{3})')
rule3 = re.compile('([#\\.]{3}/[#\\.]{3}/[#\\.]{3}) => ([#\\.]{4}/[#\\.]{4}/[#\\.]{4}/[#\\.]{4})')
import itertools


def find2x2(s:str):
    # this will be plenty fast
    # faster would be to count the number of hashes and then disambiguate the two two rules
    for _ in range(4):
        if s in rules2x2:
            return rules2x2[s]
        s = rotate2x2(s)
    raise Exception(f'could not find rule for {s}')

def find3x3(s:str):
    sf = flip3x3(s)
    for _ in range(4):
        if s in rules3x3:
            return rules3x3[s]
        if sf in rules3x3:
            return rules3x3[sf]
        s = rotate3x3(s)
        sf = rotate3x3(sf)
    raise Exception(f'could not find rule for {s}')


# parse rules
with open('Day21/input.txt') as f:
    for line in f:
        if len(line) <= 22:
            # parse as 2x2
            mat = rule2.match(line)
            if mat is None:
                exit(1)
            rules2x2[mat.group(1)]=mat.group(2)
        else:
            # parse as 3x3
            mat = rule3.match(line)
            if mat is None:
                exit(1)
            rules3x3[mat.group(1)]=mat.group(2)



current = '.#./..#/###'

current_size = 3
for i in range(5):
    if current_size % 2 == 0:
        number = int(current_size/2)
        lines = current.split('/')
        # two lines at a time
        naxt: List[str] = []
        for line1, line2 in itertools.batched(lines,2):
            nline1 = ''
            nline2 = ''
            nline3 = ''
            for i in range(0,current_size,2):
                s = line1[0+i:2+i] + '/' + line2[0+i:2+i]
                rep = find2x2(s)
                a = rep.split('/')
                nline1 += a[0]
                nline2 += a[1]
                nline3 += a[2]
            naxt.append(nline1)
            naxt.append(nline2)
            naxt.append(nline3)
        current_size = number*3
    else:
        # divide into 3x3s
        number = int(current_size / 3)
        lines = current.split('/')
        # three lines at a time
        naxt: List[str] = []
        for line1,line2,line3 in itertools.batched(lines,3):
            nline1 = ''
            nline2 = ''
            nline3 = ''
            nline4 = ''
            for i in range(0,current_size,3):
                s = line1[0+i:3+i] + '/' + line2[0+i:3+i] + '/' + line3[0+i:3+i]
                rep = find3x3(s)
                a = rep.split('/')
                nline1 += a[0]
                nline2 += a[1]
                nline3 += a[2]
                nline4 += a[3]
            naxt.append(nline1)
            naxt.append(nline2)
            naxt.append(nline3)
            naxt.append(nline4)
        current_size = number*4

    current = '/'.join(naxt)



print(current.count('#'))
