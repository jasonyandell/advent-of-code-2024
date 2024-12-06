from aoc import read_lines
import re
from collections import defaultdict

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
            incorrect.append(update)
            
    return (correct, incorrect)

def part1(lines):
    correct, _ = find_correct_and_incorrect_updates(lines)
    middle_sum = sum([update[int(len(update)/2)] for update in correct])
    return middle_sum

print("p1 sample (143):", part1(sample))
print("p1 (5268):", part1(input_text))
