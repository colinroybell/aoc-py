import pytest
from aoc2022.day02 import Run_2022_02


class Test_2022_02:
    def setup_class(self):
        self.day = Run_2022_02()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 15

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 12

    def test_regression_a(self):
        assert self.day.run_part("a") == 14375

    def test_regression_b(self):
        assert self.day.run_part("b") == 10274
