import pytest
from aoc2015.day03 import part_a, part_b


@pytest.mark.bringup
class TestBringup_2015_03:
    def test_a(self):
        assert part_a([">"]) == 2
        assert part_a(["^>v<"]) == 4
        assert part_a(["^v^v^v^v^v"]) == 2

    def test_b(self):
        assert part_b(["^v"]) == 3
        assert part_b(["^>v<"]) == 3
        assert part_b(["^v^v^v^v^v"]) == 11
