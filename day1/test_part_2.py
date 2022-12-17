from day1.part_2 import compute

INPUT_S = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

OUTPUT = 45000


def test_part_2():
    assert compute(INPUT_S) == OUTPUT
