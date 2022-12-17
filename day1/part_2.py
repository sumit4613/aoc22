import os

from main import Solution

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


class Day1Part2(Solution):
    @classmethod
    def compute(cls, input_str: str) -> int:
        total_calories_per_elf = (
            sum(int(calorie) for calorie in batch.splitlines())
            for batch in input_str.split("\n\n")
        )
        return sum(sorted(total_calories_per_elf, reverse=True)[:3])


if __name__ == "__main__":
    raise SystemExit(Day1Part2.run(INPUT_TXT))
