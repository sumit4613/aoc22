import os

from main import Solution

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

move_score = {"A": 1, "B": 2, "C": 3}
# R -> S,  P -> R, S -> P
win = {"A": "C", "B": "A", "C": "B"}
lose = {v: k for k, v in win.items()}


class Day2Part2(Solution):
    @classmethod
    def compute(cls, input_str: str) -> int:
        score = 0
        for line in input_str.splitlines():
            move_1, how_to_end_str = line.split()
            if how_to_end_str == "X":
                score += move_score[win[move_1]]
            elif how_to_end_str == "Y":
                score += move_score[move_1] + 3
            else:
                score += move_score[lose[move_1]] + 6

        return score


if __name__ == "__main__":
    raise SystemExit(Day2Part2.run(INPUT_TXT))
