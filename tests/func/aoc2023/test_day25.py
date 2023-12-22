import pytest
from aoc2023.day25 import Run_2023_25


class Test_2023_25:
    def setup_class(self):
        self.day = Run_2023_25()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 54

    def test_regression_a(self):
        assert self.day.run_part("a") == 554064

    def test_regression_b(self):
        pass
