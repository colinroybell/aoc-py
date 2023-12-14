import pytest
from aoc2023.day07 import Run_2023_07


class Test_2023_07:
    def setup_class(self):
        self.day = Run_2023_07()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 6440

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 5905

    def test_regression_a(self):
        assert self.day.run_part("a") == 251029473

    def test_regression_b(self):
        assert self.day.run_part("b") == 251003917
