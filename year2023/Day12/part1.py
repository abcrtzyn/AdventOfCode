from typing import List

def countPossibles(line: str, numbers: List[int]) -> int:
    # print(line, numbers)
    if len(line) == 0:
        # print('line is empty')
        # are there numbers left?
        if len(numbers) > 0:
            # line did not math right
            return 0
        else:
            # good job line
            return 1
    
    if line[0] == '.':
        return countPossibles(line[1:], numbers)
    elif line[0] == '#':
        # this is the first in a potential sequence
        # take the first number off and check that the number can be made
        if len(numbers) == 0:
            # print('out of numbers, impossible #')
            return 0
        n = numbers[0]
        # hash string continues far enough
        enough_hashes = len(line) >= n and line[0:n].find('.') == -1
        terminates_properly = len(line) <= n or line[n] == '.' or line[n] == '?'

        
        # [0:n+1] should look like [#?]{n}. or [#?]{n}^
        if enough_hashes and terminates_properly:
            # continuing forth
            return countPossibles(line[n+1:],numbers[1:])
        else:
            # a period was found, it is impossible to have this charecter be a hash
            # print('impossible #')
            return 0
    elif line[0] == '?':
        pos = 0;
        # try period
        # print('try period')
        pos += countPossibles(line[1:],numbers)
        # try hash
        # print('try hash')
        # this is the first in a potential sequence
        # take the first number off and check that the number can be made
        if len(numbers) == 0:
            # print('out of numbers, impossible #')
            return pos
        n = numbers[0]
        # hash string continues far enough
        enough_hashes = len(line) >= n and line[0:n].find('.') == -1
        terminates_properly = len(line) <= n or line[n] == '.' or line[n] == '?'

        # [0:n+1] should look like [#?]{n}. or [#?]{n}^
        if enough_hashes and terminates_properly:
            # continuing forth
            pos += countPossibles(line[n+1:],numbers[1:])
        else:
            # a period was found, it is impossible to have this charecter be a hash
            # print('impossible #')
            return pos
        return pos
    
    raise AssertionError('countPossibiles inaccessible code')



with open('Day12/input.txt') as f:
    count = 0
    for line in f.readlines():
        chars, numbers  = line.split()
        numbers = [int(x) for x in numbers.split(',')]
        
        count += countPossibles(chars, numbers)
    print('Part 1:',count)

    