from aoc import read_data
from collections import Counter

sample=read_data("data/11-sample.txt")
input_text=read_data("data/11.txt")

def to_dict(ns):
    result = Counter(ns)
    return result

def blink_single(n):
    if n==0: return Counter([1])
    n_str = str(n)
    digits = len(n_str)
    if digits % 2 == 0:
        half_len = int(digits/2)
        left = int(n_str[0:half_len])
        right = int(n_str[int(digits/2):])
        return Counter([left, right])
    return Counter([n*2024])

def blink(input_dict:Counter):
    combined = Counter()
    for n, count in input_dict.items():
        blink_counter = blink_single(n)
        scaled_blinks = Counter({key: value * count for key, value in blink_counter.items()})
        combined += scaled_blinks
    return combined
        
def do_blinks(input_str, times):
    input = [int(n) for n in input_str.split()]
    curr = to_dict(input)
    for n in range(times):
        curr = blink(curr)
    total = sum(v for _,v in curr.items())
    return total
    
def part1(input_str): return do_blinks(input_str, 25)
def part2(input_str): return do_blinks(input_str, 75)
print("p1 sample (55312)", part1(sample))
print("p1", part1(input_text))
print("p2", part2(input_text))