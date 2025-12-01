import pytest
from aoc2025.day01 import Run_2025_01


class Test_2025_01:
    def setup_class(self):
        self.day = Run_2025_01()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 3

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 6

    def test_bringup_b_2(self):
        # My test: goes from 50-800 rightwards (8 hits), then back to 50 leftwards (7) picking up all the combinations
        assert self.day.run_part("b", "test2") == 15

    def test_regression_a(self):
        assert self.day.run_part("a") == 1084

    def test_regression_b(self):
        assert self.day.run_part("b") == 6475
