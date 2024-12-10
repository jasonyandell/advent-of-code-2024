from aoc import read_lines
import re
from collections import defaultdict
from functools import cmp_to_key

sample=read_lines("data/05-sample.txt")
input_text=read_lines("data/05.txt")


rule_pattern = r"(\d+)\|(\d+)"

def read_input(lines):
    rules = []
    updates = []
    reading_rules = True
    for line in lines:
        if reading_rules:
            matches = re.findall(rule_pattern, line)
            if len(matches):
                a,b = matches[0]
                rules.append((int(a),int(b)))
            else:
                reading_rules = False
        else:
            updates.append([int(a) for a in line.split(',')])
    return (rules, updates)

def find_correct_and_incorrect_updates(lines):
    rules, updates = read_input(lines)
    rules_sets = [(rule, set(rule)) for rule in rules]

    correct = []
    incorrect = []
    for update in updates:
        page_set = set(update)
        applicable_rules = [rule for (rule,rule_set) in rules_sets if page_set >= rule_set]

        indices = {page: position for position, page in enumerate(update)}
        good = all(indices[earlier] < indices[later] for earlier, later in applicable_rules)

        if good: 
            correct.append(update)
        else:
            corrected = sorted(update, key=cmp_to_key(lambda a,b: ((a,b) in rules)*2-1))
            incorrect.append(corrected)

    return (correct, incorrect)

def part1(lines):
    correct, _ = find_correct_and_incorrect_updates(lines)
    middle_sum = sum([update[int(len(update)/2)] for update in correct])
    return middle_sum

def part2(lines):
    _, incorrect = find_correct_and_incorrect_updates(lines)

    middle_sum = sum([update[int(len(update)/2)] for update in incorrect])
    return middle_sum


print("p1 sample (143):", part1(sample))
print("p1 (5268):", part1(input_text))
print("p2 sample (123):", part2(sample))
print("p2:", part2(input_text))
