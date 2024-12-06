from aoc import read_lines

sample=read_lines("data/06-sample.txt")
input_text=read_lines("data/06.txt")

def parse(lines):
    blocks = set()
    guard_pos = (-1,-1)
    bounds = (0,0)
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            bounds = (max(bounds[0], row), max(bounds[1], col))
            if lines[row][col] == '#':
                blocks.add((row,col))
            if lines[row][col] == '^':
                guard_pos = (row, col)
    return bounds, guard_pos, blocks

def in_bounds(pos, bounds):
    return 0 <= pos[0] <= bounds[0] and 0 <= pos[1] <= bounds[1]

def move(pos, dir):
    return tuple(a+b for a,b in zip(pos, dir))

def part1(lines):
    bounds, guard_pos, blocks = parse(lines)
    dirs = [(-1, 0), (0,1), (1, 0), (0, -1)] # up, right, down, left
    curr_dir = 0
    positions = set()
    while in_bounds(guard_pos, bounds):
        positions.add(guard_pos)
        next = move(guard_pos, dirs[curr_dir])
        if (next in blocks):
            curr_dir = (curr_dir + 1) % 4
        else:
            guard_pos = next
    return len(positions)

print("p1 sample (41)", part1(sample))
print("p1", part1(input_text))