import pytest
from aoc2021.day25 import Run_2021_25


class Test_2021_25:
    def setup_class(self):
        self.day = Run_2021_25()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 58

    def test_bringup_b(self):
        pass

    def test_regression_a(self):
        assert self.day.run_part("a") == 337

    def test_regression_b(self):
        assert self.day.run_part("b") == True
