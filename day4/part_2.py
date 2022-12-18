import os

from main import Solution

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


class Day4Part2(Solution):
    @classmethod
    def compute(cls, input_str: str) -> int:
        n = 0
        for line in input_str.splitlines():
            ab, cd = line.split(",")
            a_s, b_s = ab.split("-")
            c_s, d_s = cd.split("-")
            a, b = int(a_s), int(b_s)
            c, d = int(c_s), int(d_s)

            if a <= c <= b or c <= a <= d:
                n += 1
        return n


if __name__ == "__main__":
    raise SystemExit(Day4Part2.run(INPUT_TXT))
