# the hardest part is converting from the triangle to one number
# then it is just 20151125*252533^(i-1)

# i ==
#    | 1   2   3   4   5   6  
# ---+---+---+---+---+---+---+
#  1 |  1   3   6  10  15  21
#  2 |  2   5   9  14  20
#  3 |  4   8  13  19
#  4 |  7  12  18
#  5 | 11  17
#  6 | 16

# I'm going to start with distance, x+y, see if that gets me anywhere
# I think that i = triangle(x+y-1)+y, something like that.

#    | 1   2   3   4   5   6  
# ---+---+---+---+---+---+---+
#  1 |  2   3   4   5   6   7
#  2 |  3   4   5   6   7
#  3 |  4   5   6   7
#  4 |  5   6   7
#  5 |  6   7
#  6 |  7




def triangle(n: int):
    return (n*(n-1)) // 2

with open('Day25/input.txt') as f:
    words = f.read().split()
    row = int(words[15].strip(','))
    col = int(words[17].strip('.'))

index = triangle(row+col-1)+col
res = (20151125 * pow(252533,index-1,33554393)) % 33554393
print('Part 1:',res)
