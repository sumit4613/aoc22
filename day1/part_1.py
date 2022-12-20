# https://adventofcode.com/2022/day/1
import os
from typing import Optional

from main import Solution

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


class Day1Part1(Solution):
    @classmethod
    def compute(cls, input_str: str) -> int:
        max_count: Optional[int] = None
        batches = input_str.split("\n\n")
        for elf_calorie_batch in batches:
            calorie_count = sum(int(calorie) for calorie in elf_calorie_batch.splitlines())
            if max_count is None or calorie_count > max_count:
                max_count = calorie_count
        return max_count

    def compute_op(self, s: str) -> int:
        # single line solution
        return max(sum(int(calorie) for calorie in batch.splitlines()) for batch in s.split("\n\n"))


if __name__ == "__main__":
    raise SystemExit(Day1Part1.run(INPUT_TXT))
