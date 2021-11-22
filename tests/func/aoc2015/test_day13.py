import pytest
from aoc2015.day13 import Run_2015_13


class Test_2015_13:
    def setup_class(self):
        self.day = Run_2015_13()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 330

    def test_bringup_b(self):
        pass

    def test_regression_a(self):
        assert self.day.run_part("a") == 733

    def test_regression_b(self):
        assert self.day.run_part("b") == 725
