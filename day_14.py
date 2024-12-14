from aoc import read_lines
import re

sample=read_lines("data/14-sample.txt")
input_text=read_lines("data/14.txt")

pattern = r"-?\d+"
def parse(text):
    bounds = [int(s) for s in text[0].split()]
    vectors = []
    for line in text[1:]:
        x,y,dx,dy = map(int, re.findall(pattern, line))
        vectors.append(((x,y,dx,dy)))
    return (bounds, vectors)

def step(state):
    [x_bound, y_bound], vectors = state
    new_vectors = []
    for x,y,dx,dy in vectors:
        x = (x + dx) % x_bound
        y = (y + dy) % y_bound
        new_vectors.append((x,y,dx,dy))
    return [x_bound, y_bound], new_vectors

def display(i, state):
    [x_bound, y_bound], vectors = state
    positions = set((row,col) for (col,row,_,_) in vectors)
    for row in range(y_bound):
        line = "" + str(i) + ":"
        for col in range(x_bound):
            if (row, col) in positions:
                line += 'X'
            else:
                line += '.'
        print(line)

def part1(text):
    state = parse(text)
    for _ in range(100):
        state = step(state)
    [x_bound, y_bound], vectors = state
    top_left = [(x,y) for (x,y,_,_) in vectors if 0<=x<x_bound // 2 and 0 <= y < y_bound // 2]
    top_right = [(x,y) for (x,y,_,_) in vectors if x_bound // 2<x<x_bound and 0 <= y < y_bound // 2]
    bottom_left = [(x,y) for (x,y,_,_) in vectors if 0<=x<x_bound // 2 and y_bound // 2 < y < y_bound]
    bottom_right = [(x,y) for (x,y,_,_) in vectors if x_bound // 2<x<x_bound and y_bound // 2 < y < y_bound]
    return len(top_left)*len(top_right)*len(bottom_left)*len(bottom_right)

def count_neighbors(vectors):
    positions = set((x,y) for (x,y,_,_) in vectors)
    total = 0
    for (x,y) in positions:
        total += \
            ((x+1,y) in positions) + \
            ((x-1,y) in positions) + \
            ((x,y+1) in positions) + \
            ((x,y-1) in positions)
    return total

def part2(text):
    state = parse(text)
    max_neighbors = 0
    best = state
    best_day = 0
    for i in range(10000):
        state = step(state)
        neighbors = count_neighbors(state[1])
        if neighbors > max_neighbors:
            max_neighbors = neighbors
            best = state
            best_day = i+1
    display(best_day, best)
    return best_day

print("p1 sample (12)", part1(sample))
print("p1", part1(input_text))
part2(sample)
part2(input_text)
