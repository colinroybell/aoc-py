import pytest
from aoc2022.day11 import Run_2022_11


class Test_2022_11:
    def setup_class(self):
        self.day = Run_2022_11()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 10605

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 2713310158

    def test_regression_a(self):
        assert self.day.run_part("a") == 56595

    def test_regression_b(self):
        assert self.day.run_part("b") == 15693274740
