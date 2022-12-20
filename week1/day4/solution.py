# Day 4: Camp Cleanup
# https://adventofcode.com/2022/day/4

from timeit import timeit

input_path = "input.txt"

# First Half
def part1():
    repeat_assignments = 0
    with open(input_path, "r") as input_file:
        for line in input_file:
            el1, el2 = line.split(",")
            el1s, el1e = map(int, el1.split("-"))
            el2s, el2e = map(int, el2.split("-"))
            if (el1s >= el2s and el1e <= el2e) or (el2s >= el1s and el2e <= el1e):
                repeat_assignments += 1
    return repeat_assignments

# Second Half 
def part2():
    repeat_assignments = 0
    with open(input_path, "r") as input_file:
        for line in input_file:
            el1, el2 = line.split(",")
            el1s, el1e = map(int, el1.split("-"))
            el2s, el2e = map(int, el2.split("-"))
            if el1s <= el2s <= el1e or el2s <= el1s <= el2e:
                repeat_assignments += 1
    return repeat_assignments

if __name__ == "__main__":
    assert part1() == 490
    assert part2() == 921

    print("TIME TAKEN : part1 = ", timeit(part1, number=1000))
    print("TIME TAKEN : part2 = ", timeit(part2, number=1000))