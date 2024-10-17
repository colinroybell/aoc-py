import pytest
from aoc2020.day05 import Run_2020_05

class Test_2020_05:
    def setup_class(self):
        self.day = Run_2020_05()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", ["FBFBBFFRLR"]) == 357

    def test_bringup_a_2(self):
        assert self.day.run_part("a", ["BFFFBBFRRR"]) == 567
        
    def test_bringup_a_3(self):
        assert self.day.run_part("a", ["FFFBBBFRRR"]) == 119
        
    def test_bringup_a_4(self):
        assert self.day.run_part("a", ["BBFFBBFRLL"]) == 820

    def test_regression_a(self):
        assert self.day.run_part("a") == 987

    def test_regression_b(self):
        assert self.day.run_part("b") == 603



