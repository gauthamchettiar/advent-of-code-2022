# https://adventofcode.com/2022/day/1

# First Half
input_path = "calories.txt"
def elf_carrying_most_calories():
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

# Second Half
def top3_elves_carrying_most_calories():
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

if __name__ == "__main__":
    assert elf_carrying_most_calories() == 68292
    assert top3_elves_carrying_most_calories() == 203203

