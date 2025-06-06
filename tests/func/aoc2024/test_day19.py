import pytest
from aoc2024.day19 import Run_2024_19


class Test_2024_19:
    def setup_class(self):
        self.day = Run_2024_19()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 6

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 16

    def test_regression_a(self):
        assert self.day.run_part("a") == 258

    def test_regression_b(self):
        assert self.day.run_part("b") == 632423618484345
