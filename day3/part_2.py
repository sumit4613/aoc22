import os

from main import Solution

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


class Day3Part2(Solution):
    @classmethod
    def compute(cls, input_str: str) -> int:
        score = 0
        items = iter(input_str.splitlines())
        while True:
            try:
                (common_item,) = set(next(items)) & set(next(items)) & set(next(items))
            except StopIteration:
                break
            else:
                if common_item.islower():
                    score += ord(common_item) - 96
                else:
                    score += ord(common_item) - 38

        return score


if __name__ == "__main__":
    raise SystemExit(Day3Part2.run(INPUT_TXT))
