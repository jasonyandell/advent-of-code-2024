from aoc import read_lines

sample=read_lines("data/07-sample.txt")
input_text=read_lines("data/07.txt")

def parse(lines):
    for line in lines:
        [total_str, item_str] = line.split(':')
        total = int(total_str)
        items = [int(s) for s in item_str.split()]
        yield (total, items)

def count_solutions_p1(total, so_far, items):
    if so_far > total: return 0 # if we've already gone too far, bail
    if (not items):
        return so_far == total # we got to the end, return whether the total is correct
    else:
        return \
            count_solutions_p1(total, so_far + items[0], items[1:]) + \
            count_solutions_p1(total, so_far * items[0], items[1:])

def part1(lines):
    return sum(
        total
        for total, items in parse(lines)
        if count_solutions_p1(total, items[0], items[1:])
    )

def count_solutions_p2(total, so_far, items):
    if so_far > total: return 0 # if we've already gone too far, bail
    if (not items):
        return so_far == total # we got to the end, return whether the total is correct
    else:
        return \
            count_solutions_p2(total, so_far + items[0], items[1:]) + \
            count_solutions_p2(total, so_far * items[0], items[1:]) + \
            count_solutions_p2(total, int(str(so_far)+str(items[0])), items[1:])

def part2(lines):
    return sum(
        total
        for total, items in parse(lines)
        if count_solutions_p2(total, items[0], items[1:])
    )

print("p1 sample (3749):", part1(sample))
print("p1:", part1(input_text)) 
print("p2 sample (11387)", part2(sample))
print("p2", part2(input_text))