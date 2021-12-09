import pytest
from aoc2021.day09 import Run_2021_09


class Test_2021_09:
    def setup_class(self):
        self.day = Run_2021_09()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 15

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 1134

    def test_regression_a(self):
        assert self.day.run_part("a") == 468

    def test_regression_b(self):
        assert self.day.run_part("b") == 1280496
