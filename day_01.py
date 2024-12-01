from aoc import read_lines
from collections import Counter

part1_sample=read_lines("data/01-p1-sample.txt")
part1_text=read_lines("data/01.txt")

def parse(lines:list):
    result = []
    for line in lines:
        result.append(list(map(int, line.split())))
    return result

def part1(pairs:list[list[int]]):
    left, right = zip(*pairs)
    left = sorted(left)
    right = sorted(right)
    distances = [abs(a-b) for a,b in zip(left, right)]
    return sum(distances)

def part2(pairs:list[list[int]]):
    counts = Counter(value for _, value in pairs)
    return sum(value * counts[value] for value, _ in pairs)

print("p1 sample: ", part1(parse(part1_sample)))
print("p1", part1(parse(part1_text)))
print("p2 sample: ", part2(parse(part1_sample)))
print("p2: ", part2(parse(part1_text)))
