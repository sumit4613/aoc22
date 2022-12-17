# https://adventofcode.com/2022/day/2
import argparse
from typing import Optional
import os

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def naaive_compute(input_str: str) -> int:
    score = 0
    move_map = {
        "A": "rock",
        "X": "rock",
        "B": "paper",
        "Y": "paper",
        "C": "scissors",
        "Z": "scissors",
    }

    move_score_map = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
        "lost": 0,
        "draw": 3,
        "won": 6,
    }
    for line in input_str.splitlines():
        move1, move2 = line.split()
        if move_map[move1] == move_map[move2]:
            # if draw
            my_move = move_map[move2]
            score += move_score_map[my_move] + move_score_map["draw"]
        elif move_map[move1] == "rock" and move_map[move2] == "paper":
            # won
            my_move = move_map[move2]
            score += move_score_map[my_move] + move_score_map["won"]
        elif move_map[move1] == "paper" and move_map[move2] == "rock":
            # lost
            my_move = move_map[move2]
            score += move_score_map[my_move] + move_score_map["lost"]
        elif move_map[move1] == "scissors" and move_map[move2] == "rock":
            # won
            my_move = move_map[move2]
            score += move_score_map[my_move] + move_score_map["won"]
        elif move_map[move1] == "rock" and move_map[move2] == "scissors":
            # lost
            my_move = move_map[move2]
            score += move_score_map[my_move] + move_score_map["lost"]
        elif move_map[move1] == "paper" and move_map[move2] == "scissors":
            # won
            my_move = move_map[move2]
            score += move_score_map[my_move] + move_score_map["won"]
        elif move_map[move1] == "scissors" and move_map[move2] == "paper":
            # lost
            my_move = move_map[move2]
            score += move_score_map[my_move] + move_score_map["lost"]

    return score


def compute(s: str) -> int:
    shape = {"R": 1, "P": 2, "S": 3}
    win = {"R": "S", "P": "R", "S": "P"}
    trans = {
        "A": "R",
        "B": "P",
        "C": "S",
        "X": "R",
        "Y": "P",
        "Z": "S",
    }
    for k, v in trans.items():
        s = s.replace(k, v)

    n = 0
    for line in s.splitlines():
        a, b = line.split()
        if a == b:
            n += 3
        elif win[a] != b:
            n += 6
        n += shape[b]
    return n


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.input_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
