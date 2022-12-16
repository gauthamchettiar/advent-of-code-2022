# https://adventofcode.com/2022/day/3

input_path = "rucksack.txt"

# First Half
def rucksack_priority():
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
def rucksack_priority_in_group():
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
    assert rucksack_priority() == 7980
    assert rucksack_priority_in_group() == 2881

