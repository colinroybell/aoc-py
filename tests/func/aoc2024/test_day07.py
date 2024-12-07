import pytest
from aoc2024.day07 import Run_2024_07


class Test_2024_07:
    def setup_class(self):
        self.day = Run_2024_07()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 3749

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 11387

    def test_regression_a(self):
        assert self.day.run_part("a") == 12839601725877

    def test_regression_b(self):
        assert self.day.run_part("b") == 149956401519484
