import pytest
from aoc2017.day05 import Run_2017_05


class Test_2017_05:
    def setup_class(self):
        self.day = Run_2017_05()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 5

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 10

    def test_regression_a(self):
        assert self.day.run_part("a") == 372671

    def test_regression_b(self):
        assert self.day.run_part("b") == 25608480
