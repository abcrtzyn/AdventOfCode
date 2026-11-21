# start on 5
number = 5
code: str = ''


with open('Day02/input.txt') as f:
    for line in f.readlines():
        
        for c in line.strip():
            match c:
                case 'U':
                    # subtract 3
                    if number > 3:
                        number -=3
                case 'D':
                    # add 3
                    if number < 7:
                        number += 3
                case 'L':
                    # subtract 1
                    if number % 3 != 1:
                        number -= 1
                case 'R':
                    # add 1
                    if number % 3 != 0:
                        number += 1
                case _:
                    assert False, 'unreachable'
        
        code += str(number)
        

print('Part 1:',code)
