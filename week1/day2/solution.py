# Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2

from timeit import timeit

input_path = "input.txt"

# First Half
def part1():
    points = 0
    with open(input_path, "r") as input_file:
        for line in input_file:
            opp_hand, player_hand = line.strip().split(" ")
            opp_hand, player_hand = ord(opp_hand)%3, ord(player_hand)%3
            
            points += player_hand if player_hand > 0 else 3
            
            if opp_hand == player_hand:
                points += 6
            elif opp_hand - player_hand in (1,-2):
                points += 3
            # win :
            # ord('C')=1, ord('A')=2, ord('B')=0
            # ord('X')=1, ord('Y')=2, ord('Z')=0
            # opp_hand == player_hand -> +6
            # draw :
            # ord('A')=2, ord('B')=0, ord('C')=1
            # ord('X')=1, ord('Y')=2, ord('Z')=0
            # opp_hand - player_hand = [1, -2, 1] -> +3
            # lose :
            # ord('B')=0, ord('C')=1, ord('A')=2
            # ord('X')=1, ord('Y')=2, ord('Z')=0
            # opp_hand - player_hand = [-1, -1, 2] -> 0
    return points

def part1_using_dict():
    points_by_strategy = { "Z": {"A":0, "B":6, "C":3, "O":3}, "Y": {"A":6, "B":3, "C":0, "O":2}, "X": {"A":3, "B":0, "C":6, "O":1} }
    points = 0
    with open(input_path, "r") as input_file:
        for line in input_file:
            opp_hand, player_hand = line.strip().split(" ")
            points += points_by_strategy[player_hand]["O"]
            points += points_by_strategy[player_hand][opp_hand]
    return points

# Second Half
def part2():
    points = 0
    with open(input_path, "r") as input_file:
        for line in input_file:
            opp_hand, strategy = line.strip().split(" ")
            opp_hand = ord(opp_hand)%3
            if strategy == "Z":
                points += opp_hand if opp_hand > 0 else 3
                points += 6
            elif strategy == "Y":
                points += (opp_hand+2)%3 if (opp_hand+2)%3 > 0 else 3
                points += 3
            else: 
                points += opp_hand + 1
            # For Z   ->   2, 0, 1   ->   2=2, 0=0, 1=1
            # For Y   ->   2, 0, 1   ->   (2+2)%3=1, (0+2)%3=2, (1+2)%3=0
            # For X   ->   2, 0, 1   ->   (2+1)=3, (0+1)=1, (1+1)=2
    return points


def part2_using_dict():
    points = 0
    points_by_strategy = { "Z": {"A":2, "B":3, "C":1, "O":6}, "Y": {"A":1, "B":2, "C":3, "O":3}, "X": {"A":3, "B":1, "C":2, "O":0} }
    with open(input_path, "r") as input_file:
        for line in input_file:
            opp_hand, strategy = line.strip().split(" ")
            points += points_by_strategy[strategy]["O"]
            points += points_by_strategy[strategy][opp_hand]
    return points



if __name__ == "__main__":
    assert part1() == 12276 
    assert part1_using_dict() == 12276
    assert part2() == 9975
    assert part2_using_dict() == 9975

    print("TIME TAKEN (W/O DICT) : part1 = ", timeit(part1, number=1000))
    print("TIME TAKEN (W/O DICT) : part2 = ", timeit(part2, number=1000))
    print("TIME TAKEN (WITH DICT) : part1_using_dict = ", timeit(part1_using_dict, number=1000))
    print("TIME TAKEN (WITH DICT) : part2_using_dict = ", timeit(part2_using_dict, number=1000))