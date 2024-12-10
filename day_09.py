from aoc import read_data
from collections import defaultdict

sample=read_data("data/09-sample.txt")
input_text=read_data("data/09.txt")

def explode(map):
    if (len(map) % 2 == 1): 
        map += "0"
    disk = []
    id = 0
    for i in range(0, len(map), 2):
        pair = map[i:i+2]
        size,free = [int(ch) for ch in pair]
        for j in range(size): disk += [[id]]
        for j in range(free): disk += [[]]
        id += 1
    return disk
            
def part1(mapx):
    disk = explode(mapx)
    start = 0
    end = len(disk)-1
    while end >= 0 and not disk[end]: end -= 1
    for start in range(len(disk)):
        if end <= start: break
        if (not disk[start]):
            disk[start], disk[end] = disk[end], disk[start]
            while end >= 0 and not disk[end]: end -= 1
    
    checksum = sum(i * value[0] for i, value in enumerate(disk) if value)

    return checksum

def part2(mapx):
    disk = explode(mapx)
    last_id = disk[-1][0]  # assuming the last one is the highest id

    files_by_id = defaultdict(list)
    for index, value in enumerate(disk):
        if value:
            files_by_id[value[0]].append(index)

    #   find gaps 
    all_gaps = [index for index, value in enumerate(disk) if value == []]
    gaps = []
    current_group = []

    # [1,2,7,8] -> [[1,2], [7,8]]
    for i in all_gaps:
        if current_group and i != current_group[-1] + 1:
            gaps.append(current_group)
            current_group = []
        current_group.append(i)

    if current_group:
        gaps.append(current_group)

    # id by id down.  look at each gap.  if the file can fit, swap it in
    for id in range(last_id, 0, -1):
        needed_files = files_by_id[id]
        needed_count = len(needed_files)
        for gap in gaps:
            if needed_count <= len(gap):
                for gap_index, file_index in zip(gap, needed_files):
                    # Only swap if file_index is not to the left (no leftward moves)
                    if file_index >= gap_index:
                        disk[gap_index], disk[file_index] = disk[file_index], disk[gap_index]
                gap[:] = gap[needed_count:]
                break

    checksum = sum(i * value[0] for i, value in enumerate(disk) if value)

    return checksum


print("p1 sample (1928):", part1(sample))
print("p1:", part1(input_text))
print("p2 sample (2858):", part2(sample))
print("p2:", part2(input_text))
