import pytest
from aoc2025.day03 import Run_2025_03, joltage, joltageN


class Test_2025_03:
    def setup_class(self):
        self.day = Run_2025_03()

    def test_joltage(self):
        assert joltage("987654321111111") == 98
        assert joltage("811111111111119") == 89
        assert joltage("234234234234278") == 78
        assert joltage("818181911112111") == 92

    def test_joltageN(self):
        assert joltageN("987654321111111", 2) == 98
        assert joltageN("811111111111119", 2) == 89
        assert joltageN("234234234234278", 2) == 78
        assert joltageN("818181911112111", 2) == 92
        assert joltageN("987654321111111", 12) == 987654321111
        assert joltageN("811111111111119", 12) == 811111111119
        assert joltageN("234234234234278", 12) == 434234234278
        assert joltageN("818181911112111", 12) == 888911112111

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 357

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 3121910778619

    def test_regression_a(self):
        assert self.day.run_part("a") == 17766

    def test_regression_b(self):
        assert self.day.run_part("b") == 176582889354075
