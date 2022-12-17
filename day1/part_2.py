import argparse
import os

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input_str: str) -> int:
    total_calories_per_elf = (
        sum(int(calorie) for calorie in batch.splitlines())
        for batch in input_str.split("\n\n")
    )
    return sum(sorted(total_calories_per_elf, reverse=True)[:3])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.input_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
