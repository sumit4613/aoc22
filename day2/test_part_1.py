from day2.part_1 import Day2Part1

INPUT_S = """\
A Y
B X
C Z
"""

OUTPUT = 15


def test_part_1():
    assert Day2Part1.compute(INPUT_S) == OUTPUT
