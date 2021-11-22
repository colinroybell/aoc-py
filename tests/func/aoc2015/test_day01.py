import pytest
from aoc2015.day01 import part_a, part_b


@pytest.mark.bringup
class TestBringup_2015_01:
    def test_a(self):
        assert part_a(["(())"]) == 0
        assert part_a(["()()"]) == 0
        assert part_a(["((("]) == 3
        assert part_a(["(()(()("]) == 3
        assert part_a(["))((((("]) == 3
        assert part_a(["())"]) == -1
        assert part_a(["))("]) == -1
        assert part_a([")))"]) == -3
        assert part_a([")())())"]) == -3

    def test_b(self):
        assert part_b([")"]) == 1
        assert part_b(["()())"]) == 5
