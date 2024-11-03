goal_col = 3029
goal_row = 2947

# going to try iterative first
x = 1
y = 1
value = 20151125
while True:
    if x == goal_col and y == goal_row:
        print(x,y, value)
        break

    if y == 1:
        y = x + 1
        x = 1
    else:
        x += 1
        y -= 1

    value = (value * 252533) % 33554393

    #if x == 7:
    #    break
    


# my value is in diagonal row 5975