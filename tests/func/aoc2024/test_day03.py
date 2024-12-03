import pytest
from aoc2024.day03 import Run_2024_03


class Test_2024_03:
    def setup_class(self):
        self.day = Run_2024_03()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 161

    def test_bringup_b(self):
        assert self.day.run_part("b", "test2") == 48

    def test_regression_a(self):
        assert self.day.run_part("a") == 182780583

    def test_regression_b(self):
        assert self.day.run_part("b") == 90772405
