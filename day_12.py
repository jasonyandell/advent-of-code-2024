from aoc import read_lines
from collections import deque, defaultdict

sample=read_lines("data/12-sample.txt")
input_text=read_lines("data/12.txt")

dirs = [(-1, 0), (0, -1), (0, 1), (1,0)] # left up right down
def get_neighbors(pos):
    row, col = pos
    return {(row+r, col+c) for (r,c) in dirs}

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

print("p1 sample (1930)", part1(sample))
print("p1", part1(input_text))
