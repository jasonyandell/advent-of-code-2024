from aoc import read_lines
from collections import deque

sample=read_lines("data/10-sample.txt")
input_text=read_lines("data/10.txt")

def get_neighbors(pos, bounds):
    r, c = pos
    surrounding = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    return set([(r,c) for (r, c) in surrounding if 0<=r<bounds[0] and 0<=c<bounds[1]])

def find_trails(grid):
    bounds = (len(grid), len(grid[0]))
    starts = [(row_idx, col_idx) for row_idx, row in enumerate(grid) for col_idx, value in enumerate(row) if value == "0"]
    horizon = deque((start, [], set()) for start in starts)

    while horizon:
        (curr, path, visited) = horizon.popleft()
        row, col = curr

        if grid[row][col] == "9":
            path.append(curr)
            yield path

        neighbors = [n for n in get_neighbors(curr, bounds) if not n in visited]

        for (r,c) in neighbors:
            if int(grid[r][c]) - int(grid[row][col]) == 1: # climbing exactly 1 higher
                horizon.append(((r,c), path + [curr], visited | {curr}))


def starts_and_trails(grid):
    starts = [(row_idx, col_idx) for row_idx, row in enumerate(grid) for col_idx, value in enumerate(row) if value == "0"]
    trails = [trail for trail in find_trails(grid)] # copy
    return starts, trails


def part1(grid):
    starts, trails = starts_and_trails(grid)
    return sum(len(set([trail[-1] for trail in trails if start == trail[0]])) for start in starts)

def part2(grid):
    starts, trails = starts_and_trails(grid)
    return sum(sum(1 for trail in trails if start == trail[0]) for start in starts)


print("p1 sample (36)", part1(sample))
print("p1", part1(input_text))
print("p2 sample (81)", part2(sample))
print("p2", part2(input_text))
