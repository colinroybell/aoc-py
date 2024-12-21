import pytest
from aoc2024.day21 import Run_2024_21


class Test_2024_21:
    def setup_class(self):
        self.day = Run_2024_21()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 126384

    def test_regression_a(self):
        assert self.day.run_part("a") == 206798

    def test_regression_b(self):
        assert self.day.run_part("b") == 251508572750680
