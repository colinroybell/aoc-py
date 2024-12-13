import pytest
from aoc2024.day13 import Run_2024_13


class Test_2024_13:
    def setup_class(self):
        self.day = Run_2024_13()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 480

    def test_regression_a(self):
        assert self.day.run_part("a") == 25751

    def test_regression_b(self):
        assert self.day.run_part("b") == 108528956728655
