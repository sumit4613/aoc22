from day2.part_2 import compute

INPUT_S = """\
A Y
B X
C Z
"""

OUTPUT = 12


def test_part_2():
    assert compute(INPUT_S) == OUTPUT
