import pytest
from aoc2024.day10 import Run_2024_10


class Test_2024_10:
    def setup_class(self):
        self.day = Run_2024_10()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", "test1") == 1

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test2") == 2

    def test_bringup_a_3(self):
        assert self.day.run_part("a", "test3") == 4

    def test_bringup_a_4(self):
        assert self.day.run_part("a", "test4") == 3

    def test_bringup_a_5(self):
        assert self.day.run_part("a", "test5") == 36

    def test_bringup_b_1(self):
        assert self.day.run_part("b", "test6") == 3

    def test_bringup_b_2(self):
        assert self.day.run_part("b", "test7") == 13

    def test_bringup_b_3(self):
        assert self.day.run_part("b", "test8") == 227

    def test_bringup_b_4(self):
        assert self.day.run_part("b", "test5") == 81

    def test_regression_a(self):
        assert self.day.run_part("a") == 593

    def test_regression_b(self):
        assert self.day.run_part("b") == 1192
