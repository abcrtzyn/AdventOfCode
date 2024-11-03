number = 5
code = 0

u = {            1:1, 
          2:2,   3:1,   4:4, 
    5:5,  6:2,   7:3,   8:4,  9:9, 
         10:6,  11:7, 12:8,
               13:11}
d = {1:3, 2:6, 3:7, 4:8, 5:5, 6:10, 7:11, 8:12, 9:9, 10:10, 11:13, 12:12, 13:13}


with open('Day02/input.txt') as f:
    for line in f.readlines():
        
        for c in line.strip():
            match c:
                case 'U':
                    number = u[number]
                case 'D':
                    number = d[number]
                case 'L':
                    # subtract 1
                    if number not in [1,2,5,10,13]:
                        number -= 1
                case 'R':
                    # add 1
                    if number not in [1,4,9,12,13]:
                        number += 1
            #print(c,number)
        code *= 16
        code += number
        #break

print(hex(code))