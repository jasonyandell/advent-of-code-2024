from aoc import read_lines
from collections import Counter

sample=read_lines("data/02-sample.txt")
part1_text = read_lines("data/02.txt")

def parse(lines:list[str]):
    results = []
    for line in lines:
        results.append(list(map(int, line.split())))
    return results

def is_one_safe(reports):
    for report in reports:
        if all(report[i] < report[i + 1] and report[i + 1]-report[i] <= 3 for i in range(len(report) - 1)):
            return True
    return False

def part1(reports:list[list[int]]):
    return sum(1 
               for report in reports 
               if is_one_safe([report, report[::-1]]))

def remove_one(array):
    return [array[:i] + array[i + 1:] for i in range(len(array))]
         
def part2(reports: list[list[int]]):
    return sum(
        1
        for report in reports
        if is_one_safe(
            [report] + remove_one(report) + 
            [report[::-1]] + remove_one(report[::-1])
        )
    )

print("p1 sample (2): ", part1(parse(sample)))
print("p1: ", part1(parse(part1_text)))
print("p1 sample (4): ", part2(parse(sample)))
print("p1: ", part2(parse(part1_text)))