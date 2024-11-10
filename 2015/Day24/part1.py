
with open('Day24/input.txt') as f:
    values = [int(x.strip()) for x in f.readlines()]
    values.reverse()

# the weight of the groups is calculatable ahead of time
group_weight = round(sum(values)/3) # it will always be an int
# print(group_weight)

number = len(values)-1

fewest_product = 100000000000000000

# i will try every possible combination of groups
# note that because we are looking for the smallest group size, if a group of size n that works shows up, i do not have to check n+1
import itertools
import functools


for i in range(2,len(values)-1): # start at 2, there is no way there are groups of 1
    # print(i)
    for x in itertools.combinations(values,i):
        if sum(x) != group_weight:
            continue
        # print(x)
        # does the rest of the weights work
        a = values.copy()
        for y in x:
            a.remove(y)
        # once we find one group, the other is good too
        for j in range(5,len(a)-4): # start at 2, there is no way there are groups of 1
            for y in itertools.combinations(a,j):
                if sum(y) == group_weight:
                    # print('this one works')
                    break
            else:
                continue
            break
        else:
            # no
            continue
        # yes
        qe = functools.reduce(lambda a,b: a*b,x)
        if qe < fewest_product:
            fewest_product = qe
    if fewest_product != 100000000000000000:
        print('Part 2:',fewest_product)
        exit()
        
    
        

            




# i = 0
# while i < combinations:
#     a_sum = values[-1]
#     a_product = values[-1]
#     a_size = 1
#     b_sum = 0
#     b_product = 1
#     b_size = 0
#     c_sum = 0
#     c_product = 1
#     c_size = 0

#     val = i
#     for x in values[:-1]:
#         match val % 3:
#             case 0:
#                 a_sum += x
#                 a_product *= x
#                 a_size += 1
#                 if a_sum > group_weight:
#                     break
#             case 1:
#                 b_sum += x
#                 b_product *= x
#                 b_size += 1
#                 if b_sum > group_weight:
#                     break
#             case 2:
#                 c_sum += x
#                 c_product *= x
#                 c_size += 1
#                 if c_sum > group_weight:
#                     break
#         val = int(val / 3)
#     else:
#         # we have made it through all values
#         #print('good work')
#         #print(a_sum,a_product,a_size)
#         #print(b_sum,b_product,b_size)
#         #print(c_sum,c_product,c_size)
#         if a_size < fewest_size or (a_size == fewest_size and a_product < fewest_product):
#             fewest_size = a_size
#             fewest_product = a_product
#         if b_size < fewest_size or (b_size == fewest_size and b_product < fewest_product):
#             fewest_size = b_size
#             fewest_product = b_product
#         if c_size < fewest_size or (c_size == fewest_size and c_product < fewest_product):
#             fewest_size = c_size
#             fewest_product = c_product

#     # we broke out of the loop
#     # this combination wont work
#     #print(a_sum,b_sum,c_sum)

#     i+=1

# print(fewest_size)
# print(fewest_product)
