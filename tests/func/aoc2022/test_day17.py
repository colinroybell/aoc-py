import pytest
from aoc2022.day17 import Run_2022_17


class Test_2022_17:
    def setup_class(self):
        self.day = Run_2022_17()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 3068

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 1514285714288

    def test_regression_a(self):
        assert self.day.run_part("a") == 3067

    def test_regression_b(self):
        assert self.day.run_part("b") == 1514369501484
