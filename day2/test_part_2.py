from day2.part_2 import Day2Part2

INPUT_S = """\
A Y
B X
C Z
"""

OUTPUT = 12


def test_part_2():
    assert Day2Part2.compute(INPUT_S) == OUTPUT
