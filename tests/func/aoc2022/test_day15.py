import pytest
from aoc2022.day15 import Run_2022_15


class Test_2022_15:
    def setup_class(self):
        self.day = Run_2022_15()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1", y=10) == 26

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1", max_coord=20) == 56000011

    def test_regression_a(self):
        assert self.day.run_part("a", y=2000000) == 4582667

    def test_regression_b(self):
        assert self.day.run_part("b") == 10961118625406
