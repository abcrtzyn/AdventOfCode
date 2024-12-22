##### various pieces of code that I used in the brute_force.py to figure out the best paths
# see the summary document.



# # trace a path backwards and return all paths
# def trace(graph, start: Tuple[str,str], end):
#     current = start
#     if current[0] == end:
#         return ['']
#     dire = current[1]
#     paths: List[str] = []

#     for next_n in graph[current]:
#         paths.extend(trace(graph,next_n,end))

#     # prepend dire
#     paths = [x+dire for x in paths]

#     return paths



### the final iteration of this code, used to see it the unique paths generated by 4 levels of inderection were possibles in all fewer levels
# yes they were

# l = ['0','A','1','2','3','4','5','6','7','8','9']
# l = ['<','^','>','v','A']

# for current in l:
#     for ch in l:
#         result4, parents4 = breadth_first_search_parents((current,'A'), is_pushed, partial(indirect_entry_neighbors,partial(indirect_entry_neighbors,partial(indirect_entry_neighbors,partial(indirect_entry_neighbors,partial(direct_entry_neighbors,arrow_neighbors_dict),arrow_neighbors_dict),arrow_neighbors_dict),arrow_neighbors_dict),arrow_neighbors_dict,ch))
#         y = trace(parents4,('P','A'),current)
#         if len(y) > 1:
#             print('not expected')
#             print(y)
#             exit(5)
#         correct_path = y[0]
#         print(current,ch,correct_path)
        

#         result1, parents1 = breadth_first_search_parents((current,'A'), is_pushed, partial(indirect_entry_neighbors,partial(direct_entry_neighbors,arrow_neighbors_dict),arrow_neighbors_dict,ch))
#         x = trace(parents1,('P','A'),current)
#         if correct_path not in x:
#             print(x)
#             print(correct_path)
#             exit(1)
#         result2, parents2 = breadth_first_search_parents((current,'A'), is_pushed, partial(indirect_entry_neighbors,partial(indirect_entry_neighbors,partial(direct_entry_neighbors,arrow_neighbors_dict),arrow_neighbors_dict),arrow_neighbors_dict,ch))
#         x = trace(parents2,('P','A'),current)
#         if correct_path not in x:
#             print(x)
#             print(correct_path)
#             exit(1)
#         result3, parents3 = breadth_first_search_parents((current,'A'), is_pushed, partial(indirect_entry_neighbors,partial(indirect_entry_neighbors,partial(indirect_entry_neighbors,partial(direct_entry_neighbors,arrow_neighbors_dict),arrow_neighbors_dict),arrow_neighbors_dict),arrow_neighbors_dict,ch))
#         x = trace(parents3,('P','A'),current)
#         if correct_path not in x:
#             print(x)
#             print(correct_path)
#             exit(1)


#         # print(parents1)
#         # exit(0)s


# this gives a nice formatted graph of parents that I could use in my network graphing tool for visual debugging
# # for k in parents:
# #     print(''.join(k))

# # print()

# # for k,v in parents.items():
# #     for x in v:
# #         print(''.join(x),', ',''.join(k),sep='')

# # print()

#         # print(current,ch,result)


# for k in parents:
#     print(''.join(k))

# print()

# for k,v in parents.items():
#     for x in v:
#         print(''.join(x),', ',''.join(k),sep='')
