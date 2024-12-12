from aoc import read_lines
from collections import deque, defaultdict

sample=read_lines("data/12-sample.txt")
input_text=read_lines("data/12.txt")

dirs = [(-1, 0), (0, -1), (0, 1), (1,0)] # left up right down
def get_neighbors(pos):
    row, col = pos
    return {(row+r, col+c) for (r,c) in dirs}

def count_consecutive(xs):
    count = 0
    previous = None
    for num in xs:
        if previous is None or num != previous + 1:
            # If this is the first element or if there's a break in consecutive sequence
            count += 1
        previous = num
    return count

def find_vertical_walls(direction_func, group, row_bounds, col_bounds):
    total = 0
    for col in range(*col_bounds):
        wall_positions = []
        for row in range(*row_bounds):
            p = (row, col)
            if p in group and direction_func(p) not in group:
                wall_positions.append(row)
        # walls at positions [1,2,5,7] = walls at [1,2], [5], [7] = 3 walls
        total += count_consecutive(wall_positions)
    return total

def find_horizontal_walls(direction_func, group, row_bounds, col_bounds):
    total = 0
    for row in range(*row_bounds):
        wall_positions = []
        for col in range(*col_bounds):
            p = (row, col)
            if p in group and direction_func(p) not in group:
                wall_positions.append(col)
        total += count_consecutive(wall_positions)
    return total

def walls(group):
    row_bounds = (min(g[0] for g in group), max(g[0] for g in group) + 1)
    col_bounds = (min(g[1] for g in group), max(g[1] for g in group) + 1)

    left = lambda pos: (pos[0], pos[1]-1)
    right = lambda pos: (pos[0], pos[1]+1)
    up = lambda pos: (pos[0]-1, pos[1])
    down = lambda pos: (pos[0]+1, pos[1])

    walls = 0
    # go down.  if you don't find anything at left or right, it's a wall
    walls += find_vertical_walls(left, group, row_bounds, col_bounds)
    walls += find_vertical_walls(right, group, row_bounds, col_bounds)

    # go across.  if you don't find anything up or down, it's a wall
    walls += find_horizontal_walls(up, group, row_bounds, col_bounds)
    walls += find_horizontal_walls(down, group, row_bounds, col_bounds)

    return walls

def perimeter(group):
    # each has a perimeter of 4 - neighbors
    total = 0
    for pos in group:
        total += 4 - len(group & get_neighbors(pos))
    return total

def flood(grid):
    todo = deque()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            todo.append( ((row, col), (row, col)) ) # consider, start
    visited = set()

    groups = defaultdict(set)
    while todo:
        (pos, start) = todo.popleft()
        if pos in visited: continue

        visited.add(pos) # seen it
        groups[start] |= set([pos]) # add it to the group

        row, col = pos

        neighbors = get_neighbors(pos) - visited # all the non-visited neighbors
        neighbors = {(r,c) for (r,c) in neighbors if 0<=r<len(grid) and 0<=c<len(grid[0])}
        if neighbors:
            for (r,c) in neighbors:
                if grid[r][c] == grid[row][col]:
                    todo.appendleft( ( (r,c), start ) )
    return groups

def part1(grid):
    groups = flood(grid)    
    groups_with_perimeters = defaultdict() | {start: (g, perimeter(g)) for (start, g) in groups.items()}

    total = 0
    for (r,c), (g, p) in groups_with_perimeters.items():
        #print(grid[r][c], len(g), p, g)
        total += len(g)*p
    return total

def part2(grid):
    groups = flood(grid)    
    groups_with_walls = defaultdict() | {start: (g, walls(g)) for (start, g) in groups.items()}

    total = 0
    for (r,c), (g, p) in groups_with_walls.items():
        #print(grid[r][c], len(g), p, g)
        total += len(g)*p
    return total

print("p1 sample (1930)", part1(sample))
print("p1", part1(input_text))
print("p2 sample (1206)", part2(sample))
print("p2", part2(input_text))
