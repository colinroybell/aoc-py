import pytest
from aoc2022.day01 import Run_2022_01


class Test_2022_01:
    def setup_class(self):
        self.day = Run_2022_01()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 24000

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 45000

    def test_regression_a(self):
        assert self.day.run_part("a") == 73211

    def test_regression_b(self):
        assert self.day.run_part("b") == 213958
