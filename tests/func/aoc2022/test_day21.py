import pytest
from aoc2022.day21 import Run_2022_21


class Test_2022_21:
    def setup_class(self):
        self.day = Run_2022_21()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 152

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 301

    def test_regression_a(self):
        assert self.day.run_part("a") == 121868120894282

    def test_regression_b(self):
        assert self.day.run_part("b") == 3582317956029
