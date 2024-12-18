from aoc import read_lines
from collections import defaultdict
import heapq

sample=read_lines("data/18-sample.txt")
input_text=read_lines("data/18.txt")

def parse(text:list[str], line_count=0):
    positions = []
    for line_number, line in enumerate(text):
        if line_count and line_number >= line_count: 
            break
        [x, y] = [int(s) for s in line.split(',')]
        positions += [(x, y)]
    return positions

def get_neighbors(pos):
    r,c = pos
    return [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

def display(positions, path, goal):
    for y in range(goal[1]+1):
        line = ""
        for x in range(goal[0+1]):
            pos = (x, y)
            if pos in positions: line += '#'
            elif pos in path: line += '+'
            else: line += '.'
        print(line)

def get_path(positions, goal):
    visited = set(positions)
    q = [(0, (0,0))]
    best_cost = defaultdict(int)
    while q:
        cost, pos = heapq.heappop(q)
        visited.add(pos)

        best = best_cost[pos]
        if best and (best <= cost): 
            continue
        best_cost[pos] = cost

        if pos == goal: 
            #display(positions, path, goal)
            return best_cost[goal]
        neighbors = [n for n in get_neighbors(pos) if \
                     n not in visited and
                     0 <= n[0] <= goal[0] and
                     0 <= n[1] <= goal[1]]
        for n in neighbors:
            heapq.heappush(q, (cost+1,n))
            
def part1(text, line_count, goal):
    positions = set(parse(text, line_count))
    return get_path(positions, goal)

def part2(text, goal):
    positions = parse(text)
    for i in range(goal[0]*goal[1]):
        line = i+1
        slice = positions[0:line]
        if not get_path(set(slice), goal):
            return str(slice[-1][0])+","+str(slice[-1][1])
    return get_path(positions, goal)

print("p1 sample (22):", part1(sample, 12, (6,6)))
print("p1:", part1(input_text, 1024, (70,70)))
print("p2 sample (6,1):", part2(sample, (6,6)))
print("p2:", part2(input_text, (70,70)))
