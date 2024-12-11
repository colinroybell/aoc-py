import pytest
from aoc2024.day11 import Run_2024_11, next_n


class Test_2024_11:
    def setup_class(self):
        self.day = Run_2024_11()

    def test_bringup_next_n(self):
        assert next_n(0) == [1]
        assert next_n(1) == [2024]
        assert next_n(10) == [1, 0]
        assert next_n(99) == [9, 9]
        assert next_n(999) == [2021976]

    def test_bringup_a_1(self):
        assert self.day.run_part("a", ["125 17"], blinks=6) == 22

    def test_bringup_a_2(self):
        assert self.day.run_part("a", ["125 17"]) == 55312

    def test_bringup_b(self):
        pass

    def test_regression_a(self):
        assert self.day.run_part("a") == 218079

    def test_regression_b(self):
        assert self.day.run_part("b") == 259755538429618
