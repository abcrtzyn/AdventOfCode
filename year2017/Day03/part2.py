INPUT = 265149

# this is all the grid I need, because the sums get quite big.
# in fact, I only need half of this

grid = [
    [145,144,143,142,141,140,139,138,137,136,135,134,133],
    [146,101,100, 99, 98, 97, 96, 95, 94, 93, 92, 91,132],
    [147,102, 65, 64, 63, 62, 61, 60, 59, 58, 57, 90,131],
    [148,103, 66, 37, 36, 35, 34, 33, 32, 31, 56, 89,130],
    [149,104, 67, 38, 17, 16, 15, 14, 13, 30, 55, 88,129],
    [150,105, 68, 39, 18,  5,  4,  3, 12, 29, 54, 87,128],
    [151,106, 69, 40, 19,  6,  1,  2, 11, 28, 53, 86,127],
    [152,107, 70, 41, 20,  7,  8,  9, 10, 27, 52, 85,126],
    [153,108, 71, 42, 21, 22, 23, 24, 25, 26, 51, 84,125],
    [154,109, 72, 43, 44, 45, 46, 47, 48, 49, 50, 83,124],
    [155,110, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,123],
    [156,111,112,113,114,115,116,117,118,119,120,121,122],
    [157,158,159,160,161,162,163,164,165,166,167,168,169]
]

totals = [[0]*15,[0]*15,[0]*15,[0]*15,[0]*15,[0]*15,[0]*15,[0]*15,[0]*15,[0]*15,[0]*15,[0]*15,[0]*15,[0]*15,[0]*15]

# calculate grid values until we find the right answer
for i in range(1,170):

    # get the grid index, by searching
    # this is easier, but it could be calculated
    for a,l in enumerate(grid):
        try:
            j = l.index(i)
        except ValueError:
            continue
        else:
            k = a
    # coordinate is (j,k)
    #print(j,k)
    
    # calculate the value of this cell
    if i==1:
        totals[k+1][j+1] = 1
    else:
        totals[k+1][j+1] = totals[k  ][j] + totals[k  ][j+1] + totals[k  ][j+2] + \
                           totals[k+1][j] +                    totals[k+1][j+2] + \
                           totals[k+2][j] + totals[k+2][j+1] + totals[k+2][j+2]
        #print(totals)
        
    # if we get to the input value, we are done
    if totals[k+1][j+1] > INPUT:
        print('finished at cell',i)
        print('Part 2:',totals[k+1][j+1])
        exit(0)

    
