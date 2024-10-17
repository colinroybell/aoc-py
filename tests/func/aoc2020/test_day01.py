import pytest
from aoc2020.day01 import Run_2020_01


class Test_2020_01:
    def setup_class(self):
        self.day = Run_2020_01()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 514579

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 241861950

    def test_regression_a(self):
        assert self.day.run_part("a") == 787776

    def test_regression_b(self):
        assert self.day.run_part("b") == 262738554
