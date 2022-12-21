# Day 7: No Space Left On Device
# https://adventofcode.com/2022/day/7

from timeit import timeit
from collections import defaultdict

input_path = "input.txt"

def get_directory_sizes() -> dict[str,dict]:
    dir = {}
    curr_dir = ""
    with open(input_path, "r") as input_file:
        for line in input_file:
            sline = line.strip().split(" ")
            if sline[0] == "$":
                if sline[1] == "cd":
                    if sline[2] == "..":
                        curr_dir = dir[curr_dir]["parent"]
                    elif sline[2] == "/":
                        dir["/"] = {"parent":None}
                        curr_dir = "/"
                    else:
                        path_str = f"/{sline[2]}" if curr_dir == "/" else f"{curr_dir}/{sline[2]}"
                        dir[path_str] = dir.get(path_str, {"parent": curr_dir})
                        curr_dir = path_str
            elif sline[0] == "dir":
                path_str = f"/{sline[1]}" if curr_dir == "/" else f"{curr_dir}/{sline[1]}"
                dir[path_str] = {"parent": curr_dir}
            else:
                t_dir = curr_dir
                while dir[t_dir]["parent"] != None:
                    dir[t_dir]["size"] = dir[t_dir].get("size", 0) + int(sline[0])
                    t_dir = dir[t_dir]["parent"]
                dir[t_dir]["size"] = dir[t_dir].get("size", 0) + int(sline[0])
    return dir

def part1(dir: dict[str,dict]):
    total = 0
    for value in dir.values():
        if value.get("size", 0) <= 100000:
            total += value.get("size", 0)
    return total

def part2(dir: dict[str,dict]):
    distance = float("inf")
    dir_size = 0
    required_size = 30000000 - (70000000 - int(dir["/"]["size"]))
    for value in dir.values():
        curr_distance = value.get("size", 0) - required_size
        if curr_distance > 0 and curr_distance < distance:
            distance = curr_distance
            dir_size = value.get("size", 0)
    return dir_size


if __name__ == "__main__":
    assert part1(get_directory_sizes()) == 1477771
    assert part2(get_directory_sizes()) ==3579501

    print("TIME TAKEN : part1 = ", timeit("part1(get_directory_sizes())", setup="from __main__ import part1, get_directory_sizes", number=1000))
    print("TIME TAKEN : part2 = ", timeit("part2(get_directory_sizes())", setup="from __main__ import part2, get_directory_sizes", number=1000))