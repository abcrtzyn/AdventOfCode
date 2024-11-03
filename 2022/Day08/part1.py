# iterate through rows and columns
# rows are easier than columns

# note that moving around in the grid is just moving a file pointer around

with open("Day08/testinput.txt") as f:
    c = f.read()
    def index(row, column):
        return c[row*100+column];
    
    # 0 to 98 both directions. remember that
    
    
    # all numbers in row 0 are visible

    # starting row 1 column 0 and moving right
    maximum = index(1,0)
    current = index(1,1)
    if current > maximum:
        # mark tree is visible
        if current == 9:
            # done, nothing higher
            pass
        maximum = current
        

