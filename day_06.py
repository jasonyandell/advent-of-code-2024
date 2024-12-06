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

def sigh_debug(bounds, guard_pos, blocks, positions, next):
    for row in range(bounds[0]+1):
        line = ""
        for col in range(bounds[1]+1):
            curr = (row, col)
            if (curr == next): line += 'X'
            elif (curr == guard_pos): line += "^"
            elif (curr in positions): line += '+'
            elif (curr in blocks): line += '#'
            else: line += '.'
        print(line)

def explore(bounds, guard_pos, blocks):
    dirs = [(-1, 0), (0,1), (1, 0), (0, -1)] # up, right, down, left
    curr_dir = 0
    positions = set()
    visited = set()
    while in_bounds(guard_pos, bounds):
        direction = dirs[curr_dir]
        positions.add(guard_pos)
        visited.add((direction, guard_pos))
        next = move(guard_pos, direction)

        if (direction, next) in visited:
            #sigh_debug(bounds, guard_pos, blocks, positions, next)
            return (positions, True)

        if (next in blocks):
            curr_dir = (curr_dir + 1) % 4
        else:
            guard_pos = next
    return (positions, False)

def part1(lines):
    bounds, guard_pos, blocks = parse(lines)
    positions, _ = explore(bounds, guard_pos, blocks)
    return len(positions)

def part2(lines):
    bounds, guard_pos, blocks = parse(lines)

    loop_count = 0

    for row in range(bounds[0]+1):
        for col in range(bounds[1]+1):
            pos = (row, col)
            if (pos not in blocks) and (pos != guard_pos):
                blocks.add(pos)
                path, loop = explore(bounds, guard_pos, blocks)
                # uncomment to see how it is progressing
                #print(row, col, len(path), loop)
                if loop: loop_count = loop_count + 1
                blocks.remove(pos)

    return loop_count

print("p1 sample (41)", part1(sample))
print("p1 (5177)", part1(input_text))
print("p2 sample (6)", part2(sample))
print("p2", part2(input_text))