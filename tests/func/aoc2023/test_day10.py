import pytest
from aoc2023.day10 import Run_2023_10

class Test_2023_10:
    def setup_class(self):
        self.day = Run_2023_10()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", "test1") == 4

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test2") == 4

    def test_bringup_a_3(self):
        assert self.day.run_part("a", "test3") == 8

    def test_bringup_a_4(self):
        assert self.day.run_part("a", "test4") == 8

    def test_bringup_b_1(self):
        assert self.day.run_part("b", "test5") == 4

    def test_bringup_b_2(self):
        assert self.day.run_part("b", "test6") == 8

    def test_bringup_b_3(self):
        assert self.day.run_part("b", "test7") == 10

    def test_regression_a(self):
        assert(self.day.run_part('a') == 6942)

    def test_regression_b(self):
        assert(self.day.run_part('b') == 297)

