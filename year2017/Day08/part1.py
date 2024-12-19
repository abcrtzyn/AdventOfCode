import re

line_rule = re.compile('(?P<reg>\\w+) (?P<dir>inc|dec) (?P<num>-?\\d+) if (?P<sub>\\w+) (?P<op>==|<|>|<=|>=|!=) (?P<comp>-?\\d+)')


registers = {}

maximum = -10000

with open('Day08/input.txt') as f:
    for line in f.readlines():
        mat = line_rule.match(line)
        if mat is None:
            print(f'could not match "{line}"')
            exit(1)
        
        res = mat.groupdict()

        if res['sub'] not in registers:
            registers[res['sub']] = 0
        if res['reg'] not in registers:
            registers[res['reg']] = 0

        action = False
        match res['op']:
            case '==':
                action = registers[res['sub']] == int(res['comp'])
            case '!=':
                action = registers[res['sub']] != int(res['comp'])
            case '<':
                action = registers[res['sub']] < int(res['comp'])
            case '>':
                action = registers[res['sub']] > int(res['comp'])
            case '<=':
                action = registers[res['sub']] <= int(res['comp'])
            case '>=':
                action = registers[res['sub']] >= int(res['comp'])

        if action:
            match res['dir']:
                case 'inc':
                    registers[res['reg']] += int(res['num'])
                case 'dec':
                    registers[res['reg']] -= int(res['num'])
        
        if registers[res['reg']] > maximum:
            maximum = registers[res['reg']]
        
# print(registers)

print(f'part 1: {max([v for k,v in registers.items()])}')
print(f'part 2: {maximum}')
