from aoc import read_lines

sample=read_lines("data/04-sample.txt")
input_text=read_lines("data/04.txt")

def part1(lines):
    target = "XMAS"
    dirs = []
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if x or y:
                dirs.append((x,y))

    count = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            for (dx,dy) in dirs:
                found = ""
                for offset in range(len(target)):
                    r = row + dx * offset
                    c = col + dy * offset
                    if r >= 0 and r < len(lines) \
                        and c >= 0 and c < len(lines[row]):
                        found += lines[r][c]
                if found == target:
                    count += 1
    return count

def part2(lines):
    masmas = [
            "M.M",
            ".A.",
            "S.S"
        ]
    sammas = [
            "S.M",
            ".A.",
            "S.M"
        ]
    massam = [
            "M.S",
            ".A.",
            "M.S"
        ]
    samsam = [
            "S.S",
            ".A.",
            "M.M"
        ]
    targets = [masmas, sammas, massam, samsam]

    count = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            for target in targets:
                found = 0
                for dr in range(len(target)):
                    for dc in range(len(target)):
                        if target[dr][dc] == ".": continue

                        r = row + dr
                        c = col + dc
                        if r >= 0 and r < len(lines) \
                            and c >= 0 and c < len(lines[row]) \
                            and target[dr][dc] == lines[r][c]:
                                found = found + 1
                if found == 5: 
                    count = count + 1

    return count

print("p1 sample (18):", part1(sample))
print("p1:", part1(input_text))
print("p2 sample (9):", part2(sample))
print("p2:", part2(input_text))
