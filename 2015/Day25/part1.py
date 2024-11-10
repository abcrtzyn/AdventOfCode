goal_col = 3029
goal_row = 2947

# going to try iterative first
x = 1
y = 1
value = 20151125
while True:
    if x == goal_col and y == goal_row:
        break

    if y == 1:
        # if at the top of the grid, go to the next diagonal
        y = x + 1
        x = 1
    else:
        # continue diagonally
        x += 1
        y -= 1

    value = (value * 252533) % 33554393

print('Part 1:',value)
