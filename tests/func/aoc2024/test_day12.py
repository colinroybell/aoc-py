import pytest
from aoc2024.day12 import Run_2024_12


class Test_2024_12:
    def setup_class(self):
        self.day = Run_2024_12()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", "test1") == 140

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test2") == 772

    def test_bringup_a_3(self):
        assert self.day.run_part("a", "test3") == 1930

    def test_bringup_b_1(self):
        assert self.day.run_part("b", "test1") == 80

    def test_bringup_b_2(self):
        assert self.day.run_part("b", "test4") == 236

    def test_bringup_b_3(self):
        assert self.day.run_part("b", "test5") == 368

    def test_bringup_b_4(self):
        assert self.day.run_part("b", "test3") == 1206

    def test_regression_a(self):
        assert self.day.run_part("a") == 1486324

    def test_regression_b(self):
        assert self.day.run_part("b") == 898684
