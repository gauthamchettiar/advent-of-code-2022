# Day 6: Tuning Trouble
# https://adventofcode.com/2022/day/6

from timeit import timeit
from collections import defaultdict

input_path = "input.txt"

# First Half
def part1():
    last_read = defaultdict(lambda:0)
    with open(input_path, "r") as input_file:
        line = input_file.readline()
        i,j = 0,1
        last_read[line[i]] = 1
        while j < len(line):
            if last_read[line[j]] > 0:
                while line[i] != line[j]:
                    last_read[line[i]] -= 1
                    i += 1
                last_read[line[i]] -= 1
                i += 1
            last_read[line[j]] += 1
            j += 1
            if j-i == 4:
                return j

def part1_using_set():
    with open(input_path, "r") as input_file:
        line = input_file.readline()
        i,j = 0, 4
        while len(set(line[i:j])) != 4:
            i+=1
            j+=1
        return j

def part2():
    last_read = defaultdict(lambda:0)
    with open(input_path, "r") as input_file:
        line = input_file.readline()
        i,j = 0,1
        last_read[line[i]] = 1
        while j < len(line):
            if last_read[line[j]] > 0:
                while line[i] != line[j]:
                    last_read[line[i]] -= 1
                    i += 1
                last_read[line[i]] -= 1
                i += 1
            last_read[line[j]] += 1
            j += 1
            if j-i == 14:
                return j

def part2_using_set():
    with open(input_path, "r") as input_file:
        line = input_file.readline()
        i,j = 0, 14
        while len(set(line[i:j])) != 14:
            i+=1
            j+=1
        return j


if __name__ == "__main__":
    assert part1() == 1723
    assert part1_using_set() == 1723
    
    assert part2() == 3708
    assert part2_using_set() == 3708

    print("TIME TAKEN : part1 = ", timeit(part1, number=1000))
    print("TIME TAKEN : part1_using_set = ", timeit(part1_using_set, number=1000))

    print("TIME TAKEN : part2 = ", timeit(part2, number=1000))
    print("TIME TAKEN : part2_using_set = ", timeit(part2_using_set, number=1000))