from io import StringIO
from typing import Dict, Set
from year2018.watchassembly.interpreter import interpret, ops, parse
from itertools import groupby
import re


sample_rule = re.compile('Before: \\[(\\d+), (\\d+), (\\d+), (\\d+)\\]\n(\\d+) (\\d+) (\\d+) (\\d+)\nAfter:  \\[(\\d+), (\\d+), (\\d+), (\\d+)\\]')

samples = []





with open('Day16/input.txt') as f:
    samplestxt = f.read().split('\n\n')
    
    program = samplestxt[-1]
    samplestxt = samplestxt[:-2]

# parse all the samples
for s in samplestxt:
    mat = sample_rule.match(s)
    if mat is None:
        print('could not parse sample')
        exit(1)
    samples.append(tuple([int(x) for x in mat.groups()]))

part1 = 0

# figure out which samples work with which instructions
maps: Dict[int,Set[str]] = {}

for instruction,samples in groupby(samples,(lambda x: x[4])):
    # print(k)
    possibles = set(ops)
    
    # for each sample with this instruction
    for sample in samples:
        regs = (sample[0],sample[1],sample[2],sample[3])
        # instruction = sample[4]
        a = sample[5]
        b = sample[6]
        c = sample[7]
        # try each operation
        # discard it as a possibility if it doesn't work
        # an optimization could be to only try ops in possibles, but this is good enough
        possible_count = 0
        for f_name in ops:
            # I'm not checking to make sure the other registers don't change
            # Every sample must behave like a normal op code, which requires this
            if ops[f_name](regs,a,b) != sample[c+8]:
                possibles.discard(f_name)
            else:
                possible_count += 1
        
        if possible_count >= 3:
            part1 += 1
        
    # add it to maps
    maps[instruction] = possibles.copy()
    

print('Part 1:',part1)

# I found it easier to output the maps and do elimination by hand than to implement a program to do it
# print(maps)

opcode_map = {}

while maps:
    # find the instruction with length 1, there should be one
    process_list = []
    for instruction in maps:
        if len(maps[instruction]) == 1:
            process_list.append(instruction)
    
    for instruction in process_list:
        opcode = maps[instruction].pop()
        opcode_map[instruction] = opcode
        del maps[instruction]
        # remove that opcode from all other maps
        for i in maps:
            maps[i].discard(opcode)

program_file = StringIO(program)

program, ip = parse(program_file,dissasemble_map=opcode_map)

assert ip is None

print('Part 2:',interpret(program)[0])
