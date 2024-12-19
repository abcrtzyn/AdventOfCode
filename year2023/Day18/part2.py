# part 1 method will no longer be suitable for tracking cell count
# lets try triangles instead

from math import atan2


org_x = 0
org_y = 0

x = org_x
y = org_y

#new_x = 0
#new_y = 0

theta = 0
area2 = 0
corner_offset2 = 0
# the last direction given
previous_direction = 3
with open('Day18/input.txt') as f:
    for line in f.readlines():
        line2 = line.split(' ')[2].strip('()#\n')
        num = int(line2, base=16)
        direction = num & 0xF
        distance = num >> 4
    # for line in f.readlines():
    #     line2 = line.split(' ')
    #     distance = int(line2[1])
    #     direction = {'U': 3, 'L': 2, 'D': 1, 'R': 0}[line[0]]
        #print(x,y,sep='\t')
        # print('dd',direction, distance)

        # use this base and the origin to make a triangle
    
        match direction:
            case 0: # R
                new_x = x + distance
                new_y = y
                height = y
                if previous_direction == 1:
                    corner_offset2 += 0.5
                else:
                    corner_offset2 -= 0.5
            case 1: # D
                new_y = y + distance
                new_x = x
                height = x
                if previous_direction == 2:
                    corner_offset2 += 0.5
                else:
                    corner_offset2 -= 0.5
            case 2: # L
                new_x = x - distance
                new_y = y
                height = y
                if previous_direction == 3:
                    corner_offset2 += 0.5
                else:
                    corner_offset2 -= 0.5
            case 3: # U
                new_y = y - distance
                new_x = x
                height = x
                if previous_direction == 0:
                    corner_offset2 += 0.5
                else:
                    corner_offset2 -= 0.5

        triangle2 = abs(height)*(distance) # height * base, also adding the edge. divide by two at the end
        #print(height,distance)

        new_theta = atan2(new_y,new_x)
        
        if new_theta >= theta or (new_theta < theta and theta > 3 and new_theta < -2.6):
            area2 += triangle2
            area2 += distance
        else:
            area2 -= triangle2
            area2 += distance
        #print(new_x,new_y,new_theta, triangle2, area2/2)
        #print(new_theta)
        # print(area2/2)

        x = new_x
        y = new_y
        theta = new_theta
        previous_direction = direction

# the last thing is to offset for inside and outside corners
# add 0.5 to area2 for every convex corner, subtract 0.5 to area2 for every concave coner
# A negative on the area shows clockwise or counterclockwise

# in counter clockwise, positive area?, right turns need to subract, left turns add

print(area2/2)
print(-corner_offset2/2)