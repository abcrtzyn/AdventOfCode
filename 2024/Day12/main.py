# grid based search followed by lots of array operations

import numpy as np


# marks all connected instances of the grid key
def search_component(grid, components, y, x, key, component_number):
    # mark cell
    components[y,x] = component_number

    # look in each direction from this cell
    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        new_y = y + dy
        new_x = x + dx
        # if out of bounds, continue
        if not (0 <= new_y < components.shape[0] and 0 <= new_x < components.shape[1]):
            continue
        # if already visited, continue
        if components[new_y,new_x] != 0:
            continue
        # if the cell isn't the right key, continue
        if grid[new_y,new_x] != key:
            continue
        search_component(grid,components,new_y,new_x,key,component_number)


with open('Day12/input.txt') as f:
    grid = np.array([list(x.strip()) for x in f.readlines()])

#### seperate out components, this will be a replacement of grid with all different numbers
component = np.zeros(grid.shape,np.int16)

current_component = 0
try:
    while True:
        current_component += 1
        # get a cell that hasn't been assigned a component number
        iy,ix = np.argwhere(component==0)[0]
        search_component(grid,component,iy,ix,grid[iy,ix],current_component)

except IndexError:
    pass

del grid

# now that we have all the components seperated, the areas are just the number of occurances of each number
# the perimeter is the number edges between the number and another number


#### calculate areas
areas = [len(np.argwhere(component==comp)) for comp in range(1,current_component)]

#### calculate permiters
perimeters = [0]*(current_component-1)

# iterate over each cell, check boundries of each cell
for y in range(component.shape[0]):
    for x in range(component.shape[1]):
        for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_y = y + dy
            new_x = x + dx
            # if out of bounds, continue
            if not (0 <= new_y < component.shape[0] and 0 <= new_x < component.shape[1]):
                perimeters[component[y,x]-1] += 1
            elif component[y,x] != component[new_y,new_x]:
                perimeters[component[y,x]-1] += 1

##### calculate number of sides
# for each row (and each column)
    # for each column (and each row)
        # look at each pair
        # if it is different from the previous pair, 
            # add the sides to both regions

number_of_sides = [0]*(current_component-1)

# first is to mark down all the grid edges
edge_prev1 = None
edge_prev2 = None
for i in range(component.shape[0]):
    curr1 = component[i,0]
    curr2 = component[i,-1]

    if curr1 != edge_prev1:
        number_of_sides[curr1-1] += 1
        edge_prev1 = curr1

    if curr2 != edge_prev2:
        number_of_sides[curr2-1] += 1
        edge_prev2 = curr2

edge_prev1 = None
edge_prev2 = None
for j in range(component.shape[1]):
    curr1 = component[0,j]
    curr2 = component[-1,j]

    if curr1 != edge_prev1:
        number_of_sides[curr1-1] += 1
        edge_prev1 = curr1

    if curr2 != edge_prev2:
        number_of_sides[curr2-1] += 1
        edge_prev2 = curr2


# now pairs
for i in range(component.shape[0]-1):
    prev_a = None
    prev_b = None
    for j in range(component.shape[1]):
        curr_a = component[i,j]
        curr_b = component[i+1,j]
        if curr_a == curr_b:
            prev_a = curr_a
            prev_b = curr_b
            continue

        if curr_a != prev_a or prev_a == prev_b:
            number_of_sides[curr_a-1] += 1
        
        if curr_b != prev_b or prev_a == prev_b:
            number_of_sides[curr_b-1] += 1

        prev_a = curr_a
        prev_b = curr_b

       
for j in range(component.shape[0]-1):
    prev_a = None
    prev_b = None
    for i in range(component.shape[1]):
        curr_a = component[i,j]
        curr_b = component[i,j+1]
        if curr_a == curr_b:
            prev_a = curr_a
            prev_b = curr_b
            continue

        if curr_a != prev_a or prev_a == prev_b:
            number_of_sides[curr_a-1] += 1
        
        if curr_b != prev_b or prev_a == prev_b:
            number_of_sides[curr_b-1] += 1

        prev_a = curr_a
        prev_b = curr_b



print('Part 1:',sum(x*y for x,y in zip(areas,perimeters)))
print('Part 2:',sum(x*y for x,y in zip(areas,number_of_sides)))
