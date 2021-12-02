import pytest
from aoc2021.day02 import Run_2021_02


class Test_2021_02:
    def setup_class(self):
        self.day = Run_2021_02()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 150

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 900

    def test_regression_a(self):
        assert self.day.run_part("a") == 1383564

    def test_regression_b(self):
        assert self.day.run_part("b") == 1488311643
