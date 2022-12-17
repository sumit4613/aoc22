from day2.part_1 import compute

INPUT_S = """\
A Y
B X
C Z
"""

OUTPUT = 15


def test_part_1():
    assert compute(INPUT_S) == OUTPUT
