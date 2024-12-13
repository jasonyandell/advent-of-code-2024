from aoc import read_lines
import re

sample=read_lines("data/13-sample.txt")
input_text=read_lines("data/13.txt")

# thank you ChatGPT
def extract_numbers(line):
    # Split the line into parts and filter only the numeric ones
    return [int(part.strip('X+Y=,')) for part in line.split() if any(char.isdigit() for char in part)]

def parse(text:list[str], increase=0):
    records = []
    for line in text:
        if line.startswith('Button A'):
            x1,y1 = extract_numbers(line)
        if line.startswith('Button B'):
            x2,y2 = extract_numbers(line)
        if line.startswith('Prize'):
            s1,s2 = extract_numbers(line)
        if line == '':
            records.append( ([x1, x2, s1+increase, y1, y2, s2+increase] ) )
    records.append( ([x1, x2, s1+increase, y1, y2, s2+increase] ) )
    return records

def solve_line(record):
    A,B,C,D,E,F = record
    no_solution = (False, [])

    denominator = A*E - B*D  # (94*67 - 34*22)

    if denominator == 0:
        return no_solution
    else:
        # Solve using Cramer's rule (thanks again, ChatGPT)
        X_numerator = (C*E - B*F)
        X = X_numerator / denominator
        if (X_numerator % denominator != 0): return no_solution # thanks Reddit for the modulo trick
        Y_numerator = (A*F - C*D)
        Y = Y_numerator / denominator
        if (Y_numerator % denominator != 0): return no_solution
        return (True, [int(X),int(Y)])

def part1(text):
    records = parse(text)
    total = 0
    for record in records:
        valid, solution = solve_line(record)
        if valid:
            total += solution[0]*3 + solution[1]
    return total

def part2(text):
    records = parse(text, 10000000000000)
    total = 0
    for i, record in enumerate(records):
        valid, solution = solve_line(record)
        if valid:
            total += solution[0]*3 + solution[1]
    return total

print("p1 sample (480)", part1(sample))
print("p1", part1(input_text))
print("p2 sample (???)", part2(sample))
print("p2", part2(input_text))