from aoc import read_lines

sample=read_lines("data/08-sample.txt")
input_text=read_lines("data/08.txt")

def antinodes(start, end, single):
    sr, sc = start
    er, ec = end
    dr, dc = (er-sr, ec-sc)
    if (single):
        forward = (er+dr, ec+dc)
        backward = (sr-dr, sc-dc)
        return set([forward, backward])
    else:
        result = set()
        for i in range(255):
            forward = (er+dr*i, ec+dc*i)
            backward = (sr-dr*i, sc-dc*i)
            result.add(forward)
            result.add(backward)
        return result

def print_grid(lines, coords):
    for r in range(len(lines)):
        line = ""
        for c in range(len(lines[0])):
            if (r, c) in coords: line += "#"
            else: line += lines[r][c]
        print(line)

def big_o_n_4th_go(lines, single):
    found = set()
    rows = len(lines)
    cols = len(lines[0])
    for from_row in range(rows):
        for from_col in range(cols):
            if lines[from_row][from_col] == ".": continue
            for to_row in range(from_row, rows):
                for to_col in range(cols):
                    if from_row == to_row and from_col == to_col: continue
                    if lines[from_row][from_col] == lines[to_row][to_col]:
                        found |= antinodes((from_row, from_col), (to_row, to_col), single)
    in_bounds = [(r,c) for (r,c) in found if 0<=r<rows and 0<=c<cols]
    # print_grid(lines, in_bounds)
    return in_bounds

def part1(lines):
    coords = big_o_n_4th_go(lines, True)
    return len(coords)

def part2(lines):
    coords = big_o_n_4th_go(lines, False)
    return len(coords)

print("p1 sample (14)", part1(sample))
print("p1", part1(input_text))
print("p2 sample (34)", part2(sample))
print("p2", part2(input_text))
