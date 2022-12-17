# https://adventofcode.com/2022/day/1
import argparse
from typing import Optional
import os

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input_str: str) -> int:
    max_count: Optional[int] = None
    batches = input_str.split("\n\n")
    for elf_calorie_batch in batches:
        calorie_count = sum(int(calorie) for calorie in elf_calorie_batch.splitlines())
        if max_count is None or calorie_count > max_count:
            max_count = calorie_count
    return max_count


def compute_op(s: str) -> int:
    # single line solution
    return max(
        sum(int(calorie) for calorie in batch.splitlines()) for batch in s.split("\n\n")
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.input_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
