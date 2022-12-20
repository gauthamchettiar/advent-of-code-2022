# Day 5: Supply Stacks
# https://adventofcode.com/2022/day/5

from timeit import timeit
from collections import defaultdict
from collections import deque
from re import compile

input_stack_path = "input_stack.txt"
input_operation_path = "input_operation.txt"

# Helper methods
def read_stack():
    stacks = defaultdict(lambda: [])
    with open(input_stack_path, "r") as input_file:
        for line in input_file:
            line = line.strip("\n")
            stack_number = 0
            empty_places = 0
            for crates in line.split(" "):
                if len(crates) == 0:
                    empty_places += 1
                elif len(crates) == 3:
                    stack_number += (empty_places // 4) + 1
                    stacks[stack_number].append(crates[1])
                    empty_places = 0
                elif len(crates) == 1:
                    stacks[int(crates)] = deque(reversed(stacks[int(crates)]))
    return stacks

def read_list():
    return {key:list(value) for key, value in read_stack().items()}

# First Half
def part1(stacks:dict[str, deque]):
    reg = compile("move (\d+) from (\d+) to (\d+)")
    with open(input_operation_path, "r") as input_file:
        for line in input_file:
            ext = list(map(int, reg.match(line).groups()))
            for _ in range(ext[0]):
                stacks[ext[2]].append(stacks[ext[1]].pop())
    output = ""
    for i in range(len(stacks)):
        output += stacks[i+1].pop()
    return output

def part1_with_list(stacks:dict[str, list]):
    reg = compile("move (\d+) from (\d+) to (\d+)")
    with open(input_operation_path, "r") as input_file:
        for line in input_file:
            ext = list(map(int, reg.match(line).groups()))
            stacks[ext[2]].extend(reversed(stacks[ext[1]][-ext[0]:]))
            stacks[ext[1]] = stacks[ext[1]][:-ext[0]]
    output = ""
    for i in range(len(stacks)):
        output += stacks[i+1].pop()
    return output

# Second Half
def part2(stacks:dict[str, list]):
    reg = compile("move (\d+) from (\d+) to (\d+)")
    with open(input_operation_path, "r") as input_file:
        for line in input_file:
            ext = list(map(int, reg.match(line).groups()))
            stacks[ext[2]].extend(stacks[ext[1]][-ext[0]:])
            stacks[ext[1]] = stacks[ext[1]][:-ext[0]]
    output = ""
    for i in range(len(stacks)):
        output += stacks[i+1].pop()
    return output

if __name__ == "__main__":
    assert part1(read_stack()) == "HNSNMTLHQ"
    assert part1_with_list(read_list()) == "HNSNMTLHQ"
    assert part2(read_list()) == "RNLFDJMCT"

    print("TIME TAKEN (WITH DEQUE) : part1 = ", timeit("stack_dict = read_stack(); part1(stack_dict)", setup="from __main__ import part1, read_stack", number=1000))
    print("TIME TAKEN (WITH LIST) : part1_with_list = ", timeit("list_dict = read_list(); part1_with_list(list_dict)", setup="from __main__ import part1_with_list, read_list", number=1000))
    print("TIME TAKEN (WITH LIST) : part1 = ", timeit("list_dict = read_list(); part2(list_dict)", setup="from __main__ import part2, read_list", number=1000))







