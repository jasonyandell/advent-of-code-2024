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

    # id by id down
    for id in range(last_id, 0, -1):
        print(id)
        #   find gaps 
        all_gaps = [index for index, value in enumerate(disk) if value == []]
        gaps=[]
        gap = []
        gaps.append(gap)
        for index in all_gaps:
            if not gap:
                gap.append(index) # collect 
                continue
            if index == gap[-1]+1: 
                gap.append(index)
            else: 
                gap = [index]
                gaps.append(gap)

        # foreach gap 
        for gap in gaps:
            # if file can fit (len(diles_by_id[id]))
            if len(files_by_id[id])<=len(gap):
                # swap it in, index in files_by_id[id]
                files_indexes = files_by_id[id]
                for i in range(len(files_indexes)):
                    gap_index = gap[i]
                    file_index = files_indexes[i]
                    if file_index < gap_index: 
                        continue # don't look at leftward-moves
                    disk[gap_index], disk[file_index] = disk[file_index], disk[gap_index]
                break

        # output = ""
        # for value in disk:
        #     if not value: output += "."
        #     else: output += str(value[0] % 10)
        #print(id, output)

    checksum = sum(i * value[0] for i, value in enumerate(disk) if value)

    return checksum


print("p1 sample (1928):", part1(sample))
print("p1:", part1(input_text))
print("p2 sample (2858):", part2(sample))
print("p2:", part2(input_text))
