score = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

with open('Day04/input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        checksum = line[line.find('['):][1:-1]
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
        
        check = [x[0] for x in sorted(sorted(freq.items(),key=lambda x:x[0]),key=lambda x:x[1],reverse=True)[:5]]
        #print(check)

        for a,b in zip(check,checksum):
            if a != b:
                break
        else:
            # this one is good
            score += number
            shift = number % 26
            shifted = str.maketrans(alphabet+'-',alphabet[shift:] + alphabet[:shift] +' ','0123456789')
            name = line[:line.find('[')].translate(shifted)
            print(name,number)

print(score)

        
        

