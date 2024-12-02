import pytest
from aoc2024.day02 import Run_2024_02


class Test_2024_02:
    def setup_class(self):
        self.day = Run_2024_02()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 2

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 4

    def test_regression_a(self):
        assert self.day.run_part("a") == 282

    def test_regression_b(self):
        assert self.day.run_part("b") == 349
