import pytest
from aoc2015.day09 import Run_2015_09


class Test_2015_09:
    def setup_class(self):
        self.day = Run_2015_09()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 605

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 982

    def test_regression_a(self):
        assert self.day.run_part("a") == 207

    def test_regression_b(self):
        assert self.day.run_part("b") == 804
