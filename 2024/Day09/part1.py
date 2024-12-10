# the quick way of doing this problem involves pointers on both ends of the string

# things we need to know
# how many files are there
# what is the parity of file/free

# go through the disk map char by char
# things to keep track of
# the id and length of the current last file

# if the char is a file
# add the id*current pos for length of file
# else, char is free space
# 

def file_id(disk_map_ptr):
    if disk_map_ptr % 2 == 0:
        return disk_map_ptr // 2
    else:
        raise Exception('file_id was given an odd disk_map_ptr, which is in free space')


with open('Day09/input.txt') as f:
    s = f.read().strip()
    length = len(s)
    if length % 2 == 0:
        raise Exception('This program was not fully designed to handle even length inputs')
    
    # going through the disk map backwards
    remo_ptr = length + 1
    length_left = 0
    checksum = 0
    curr_disk_pos = 0
    
    # this loop will break early
    for curr_ptr in range(length):
        # each loop handles one file or one empty space
        if remo_ptr == curr_ptr:
            print(curr_ptr)
            # there are only (length_left) cells to place
            for _ in range(length_left):
                checksum += curr_disk_pos * file
                curr_disk_pos += 1
            break

        if curr_ptr % 2 == 0:
            # handle an in place file
            file_len = int(s[curr_ptr])

            # TODO find a better expression for this
            file = file_id(curr_ptr)
            for _ in range(file_len):
                checksum += curr_disk_pos * file
                curr_disk_pos += 1

        else:
            # handle free space from the reverse side
            free_space = int(s[curr_ptr])
            
            while free_space:
                if length_left != 0:
                    cells = min(free_space,length_left)
                    free_space -= cells
                    length_left -= cells
                    # modify checksum with (cells) entries of (file_id(remo_ptr))
                    file = file_id(remo_ptr)
                    for _ in range(cells):
                        checksum += curr_disk_pos * file
                        curr_disk_pos += 1
                else:
                    # this file is done, get the next one
                    remo_ptr -= 2
                    length_left = int(s[remo_ptr])
                    if remo_ptr == curr_ptr:
                        print('the end pointer has reached the current pointer')
                        print('I do not know what this situation looks like because the test input and my input did not have this come up')
                        print('It may never occur as far as I know')
                        exit(1)


print(checksum)
