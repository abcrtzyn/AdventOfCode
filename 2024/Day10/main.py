# pretty simple backtracking search problem


from typing import Set, Tuple


with open('2024/Day10/input.txt') as f:
    grid = [x.strip() for x in f.readlines()]


# given the current coordinate in the grid
# returns a set of all the 9s reached and the number of paths that can reach each endpoint
def score(y,x) -> Tuple[Set[Tuple[int,int]],int]:
    digit = int(grid[y][x])

    if digit == 9:
        # this is a good path
        return (set([(y,x)]),1)

    trail_ends: Set[Tuple[int,int]] = set()
    total_paths: int = 0

    # from (y,x), try each direction
    for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        new_y = y + dy
        new_x = x + dx
        # check limits
        if not (0 <= new_y < len(grid) and 0 <= new_x < len(grid[0])):
            continue

        if int(grid[new_y][new_x]) == digit + 1:
            endpoints, paths = score(new_y,new_x)
            trail_ends = trail_ends.union(endpoints)
            total_paths += paths

    return (trail_ends,total_paths)


part1_score = 0
part2_score = 0

for i,line in enumerate(grid):
    for j,char in enumerate(line):
        if char == '0':
            endpoints, paths = score(i,j)
            part1_score += len(endpoints)
            part2_score += paths

print('Part 1:',part1_score)
print('Part 2:',part2_score)
