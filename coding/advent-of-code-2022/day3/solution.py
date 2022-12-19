# Day 3: Rucksack Reorganization
# https://adventofcode.com/2022/day/3

from timeit import timeit

input_path = "input.txt"

# First Half
def part1():
    priority = 0
    with open(input_path, "r") as input_file:
        for line in input_file:
            midpoint = len(line)//2
            common_character = "".join(set(line[:midpoint]).intersection(set(line[midpoint:])))
            if ord(common_character) > 96:
                priority += ord(common_character) - 96
            else:
                priority += ord(common_character) - 38
    return priority

# Second Half
def part2():
    priority = 0
    with open(input_path, "r") as input_file:
        three_lines = [None, None, None]
        for lno, line in enumerate(input_file):
            line = line.strip()
            three_lines[lno%3] = set(line)
            if lno % 3 == 2:
                common_character = "".join(set.intersection(*three_lines))
                if ord(common_character) > 96:
                    priority += ord(common_character) - 96
                else:
                    priority += ord(common_character) - 38
    return priority

if __name__ == "__main__":
    assert part1() == 7980
    assert part2() == 2881
    
    print("TIME TAKEN (NOT OPTIMIZED) : part1 = ", timeit(part1, number=1000))
    print("TIME TAKEN (NOT OPTIMIZED) : part2 = ", timeit(part2, number=1000))

