import pytest
from aoc2015.day04 import Run_2015_04


class Test_2015_04:
    def setup_class(self):
        self.day = Run_2015_04()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", ["abcdef"]) == 609043

    def test_bringup_a_2(self):
        assert self.day.run_part("a", ["pqrstuv"]) == 1048970

    def test_bringup_b(self):
        pass

    def test_regression_a(self):
        assert self.day.run_part("a") == 282749

    def test_regression_b(self):
        assert self.day.run_part("b") == 9962624
