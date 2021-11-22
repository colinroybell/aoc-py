import pytest


@pytest.mark.regression
class TestRegression2015:
    def test_01(self):
        from aoc2015.day01 import part_a, part_b

        assert part_a("data/aoc2015/day01.txt") == 280
        assert part_b("data/aoc2015/day01.txt") == 1797

    def test_03(self):
        from aoc2015.day03 import part_a, part_b

        assert part_a("data/aoc2015/day03.txt") == 2081
        assert part_b("data/aoc2015/day03.txt") == 2341
