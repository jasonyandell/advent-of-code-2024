from aoc import read_data
import re

p1_sample=read_data("data/03-sample.txt")
p2_sample=read_data("data/03-p2-sample.txt")
input_text=read_data("data/03.txt")

def part1(input):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input)
    numbers = [(int(a), int(b)) for a,b in matches]
    return sum(a*b for (a,b) in numbers)

def part2(input):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)"
    matches = re.findall(pattern, input)
    enabled = True
    total = 0
    for (a,b,do,don) in matches:
        if a and b and enabled: total += int(a)*int(b)
        if do: enabled = True
        if don: enabled = False
    return total


print("p1 sample (161):", part1(p1_sample))
print("p1:", part1(input_text))
print("p2 sample (48):", part2(p2_sample))
print("p2:", part2(input_text))
