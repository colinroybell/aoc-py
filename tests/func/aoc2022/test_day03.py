import pytest
from aoc2022.day03 import Run_2022_03


class Test_2022_03:
    def setup_class(self):
        self.day = Run_2022_03()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 157

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 70

    def test_regression_a(self):
        assert self.day.run_part("a") == 7908

    def test_regression_b(self):
        assert self.day.run_part("b") == 2838
