import pytest
from aoc2023.day18 import Run_2023_18


class Test_2023_18:
    def setup_class(self):
        self.day = Run_2023_18()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", "test1") == 62

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test2") == 12

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 952408144115

    def test_regression_a(self):
        assert self.day.run_part("a") == 62500

    def test_regression_b(self):
        assert self.day.run_part("b") == 122109860712709
