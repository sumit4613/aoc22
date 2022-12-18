from day4.part_2 import Day4Part2

INPUT_S = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

OUTPUT = 4


def test_part_2():
    assert Day4Part2.compute(INPUT_S) == OUTPUT
