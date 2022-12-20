# https://adventofcode.com/2022/day/3
import collections
import os

from main import Solution

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


class Day3Part1(Solution):
    @classmethod
    def compute(cls, input_str: str) -> int:
        n = 0
        for line in input_str.splitlines():
            first_half, second_half = line[: len(line) // 2], line[len(line) // 2 :]
            first_half_count, second_half_count = collections.Counter(
                first_half,
            ), collections.Counter(second_half)
            (common_item,) = first_half_count & second_half_count
            if common_item.islower():
                n += 1 + ord(common_item) - ord("a")
            else:
                n += 27 + ord(common_item) - ord("A")
        return n


if __name__ == "__main__":
    raise SystemExit(Day3Part1.run(INPUT_TXT))
