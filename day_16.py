from aoc import read_lines
import heapq

sample=read_lines("data/16-sample.txt")
input_text=read_lines("data/16.txt")

NORTH = (-1,0)
SOUTH = (1,0)
WEST = (0,-1)
EAST = (0,1)
dirs = [EAST, SOUTH, WEST, NORTH]

def parse(text):
    walls = set()
    for row, row_text in enumerate(text):
        for col, curr_char in enumerate(row_text):
            if curr_char == '#':
                walls.add( (row, col) )
            if curr_char == 'S':
                start = ((row, col), 0)
            if curr_char == 'E':
                end = (row, col)
    return (start, end, walls)

def costs(position):
    p, d = position
    left = (1000, (p, (d - 1) % 4))
    right = (1000, (p, (d + 1) % 4))
    forward = (1, ((p[0] + dirs[d][0], p[1] + dirs[d][1]), d))
    return left, forward, right

def get_paths(text):
    start, end, walls = parse(text)

    good_paths = []

    #                cost, position, path, visited
    horizon = [(0, start, [], set())]
    while horizon:
        cost, position, path, visited = heapq.heappop(horizon)
        visited |= {position} # new visited with this position in it
        p, d = position

        path = path + [position]
        
        if p == end: 
            good_paths += [(cost, path)]

        neighbors = [c for c in costs(position) if (c[1] not in visited) and (c[1][0] not in walls)]

        for n in neighbors:
            n_cost, n_pos = n
            heapq.heappush(horizon, (cost + n_cost, n_pos, path, visited)) # new cost, new position, path to here + curr

    min_cost = min(c[0] for c in good_paths)
    return [p for p in good_paths if p[0] == min_cost]

def part1(text):
    paths = get_paths(text)
    return paths[0][0]

def part2(text):
    paths = get_paths(text)
    positions = set()
    for cost, path in paths:
        for pos in path:
            positions |= {pos[0]}
    return len(positions)

        
print("p1 sample (11048)", part1(sample))
print("p1", part1(input_text))
print("p2 sample (64)", part2(sample))
print("p2", part2(input_text))

