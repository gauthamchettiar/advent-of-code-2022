# Day 1: Calorie Counting
# https://adventofcode.com/2022/day/1

from timeit import timeit

input_path = "input.txt"

# First Half
def part1():
    max_value = 0
    curr_value = 0
    
    with open(input_path, "r") as input_file:
        for line in input_file:
            if line == "\n":
                max_value = curr_value if curr_value > max_value else max_value
                curr_value = 0
            else:
                curr_value += int(line)
    return max_value

def part1_using_list():
    sum_of_individual_calories = []
    
    with open(input_path, "r") as input_file:
        calories = []
        for line in input_file:
            if line == "\n":
                sum_of_individual_calories.append(sum(calories))
                calories = []
            else:
                calories.append(int(line))
    return max(sum_of_individual_calories)

# Second Half
def part2():
    max_value = [0, 0, 0]
    lowest_index = 0
    curr_value = 0
    
    with open(input_path, "r") as input_file:
        for line in input_file:
            if line == "\n":
                lowest_value = float("inf")
                for i in range(3):
                    if max_value[i] < lowest_value:
                        lowest_value = max_value[i]
                        lowest_index = i
                if curr_value > lowest_value:
                    max_value[lowest_index] = curr_value                     
                curr_value = 0
            else:
                curr_value += int(line)
    return sum(max_value)

def part2_using_list():
    sum_of_individual_calories = []
    
    with open(input_path, "r") as input_file:
        calories = []
        for line in input_file:
            if line == "\n":
                sum_of_individual_calories.append(sum(calories))
                calories = []
            else:
                calories.append(int(line))
    return sum(sorted(sum_of_individual_calories, reverse=True)[:3])

if __name__ == "__main__":
    assert part1() == 68292
    assert part1_using_list() == 68292
    assert part2() == 203203
    assert part2_using_list() == 203203

    print("TIME TAKEN (W/O LIST) : part1 = ", timeit(part1, number=1000))
    print("TIME TAKEN (W/O LIST) : part2 = ", timeit(part2, number=1000))
    print("TIME TAKEN (WITH LIST) : part1_using_list = ", timeit(part1_using_list, number=1000))
    print("TIME TAKEN (WITH LIST) : part2_using_list = ", timeit(part2_using_list, number=1000))