# moving whole files is quite different
# I think it will be best to store locations and the amount of free space that location has

# Attempt to move a file
# find a free space that has more than needed space and is the smallest position
# keeping lists of all free spaces of each size (1-9, plus extra) allows finding the smallest index in near O(1) time

# as soon as a file is placed, it can contribute to the checksum

from typing import Dict, List
import heapq

# dictionary of (free space length: list of start indicies heap sorted)
free_spaces: Dict[int,List[int]]= {}

def add_free_space(ptr: int, length: int):
    if length not in free_spaces:
        free_spaces[length] = []
    
    heapq.heappush(free_spaces[length],ptr)


def file_id(disk_map_ptr):
    if disk_map_ptr % 2 == 0:
        return disk_map_ptr // 2
    else:
        raise Exception('file_id was given an odd disk_map_ptr, which is in free space')
    
def compute_checksum_contribution(disk_ptr, f_id, file_length):
    # with (id) at (disk_ptr)
    # sum the values disk_ptr, disk_ptr + 1, disk_ptr + 2 up to disk_ptr + file_length
    # = disk_ptr * file_length + (trianglular number for file_length - 1)
    # return f_id * sum(range(disk_ptr,disk_ptr+file_length))
    return f_id * (disk_ptr * file_length + (file_length - 1)*(file_length) // 2)



with open('Day09/input.txt') as f:
    s = f.read().strip()
    # mark down free spaces
    disk_ptr = 0

    for map_ptr in range(len(s)):
        block = int(s[map_ptr])
        if map_ptr % 2 != 0:
            if block == 0:
                continue
            # free space
            add_free_space(disk_ptr,block)
        # file or free space
        disk_ptr += block

    # print(free_spaces)
    #print(disk_ptr)

    if (len(s)) % 2 == 0:
        raise Exception('even length input string, not expecting that')


    # now, go through all files in reverse and try to place them
    # there is no need to track free spaces after a file that is placed
    # no other file is allowed to use that space
    checksum = 0

    # go through map backwards
    for map_ptr in range(len(s)-1,-1,-1):
        block = int(s[map_ptr])
        disk_ptr -= block
        if map_ptr % 2 != 0:
            continue
        #print(file_id(map_ptr))
        # go through each free space length that is greater than (block)
        # find the one with the smallest index
        smallest_index = 9999999
        smallest__key = 0
        for k in free_spaces:
            if k >= block:
                # look at the smallest element
                if free_spaces[k]:
                    test = free_spaces[k][0]
                    if test < smallest_index:
                        smallest_index = test
                        smallest__key = k
        
        if smallest__key != 0 and smallest_index > disk_ptr:
            # it is to the right of the file
            # since it is the smallest index, all other free spaces larger than this size are unavailable
            # delete all of these
            for i in range(smallest__key,10):
                if i in free_spaces:
                    del free_spaces[i]
            # show that this block does not move
            smallest__key = 0


        if smallest__key == 0:
            checksum += compute_checksum_contribution(disk_ptr,file_id(map_ptr),block)
            
        else:
            # found a spot for this file
            heapq.heappop(free_spaces[smallest__key])
            if smallest__key != block:
                add_free_space(smallest_index+block,smallest__key-block)

            checksum += compute_checksum_contribution(smallest_index,file_id(map_ptr),block)
        #print(free_spaces)



print(checksum)
