score = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

with open('Day04/input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        # get the checksum
        checksum = line[line.find('['):][1:-1]
        
        # make a frequency table
        freq = {}
        number = 0
        for c in line:
            if c == '-':
                continue
            if c.isdigit():
                number *= 10
                number += int(c)
                continue
            if c == '[':
                break
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        # create the sorted list of letters
        check = [x[0] for x in sorted(sorted(freq.items(),key=lambda x:x[0]),key=lambda x:x[1],reverse=True)[:5]]
        
        # check that it is correct
        for a,b in zip(check,checksum):
            if a != b:
                break
        else:
            # this one is good
            score += number
            # decode the name
            shift = number % 26
            shifted = str.maketrans(alphabet+'-',alphabet[shift:] + alphabet[:shift] +' ','0123456789')
            name = line[:line.find('[')].translate(shifted)
            if 'north' in name:
                print(name)
                print('Part 2:',number)

print(score)

        
        
