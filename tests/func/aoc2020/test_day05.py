import pytest
from aoc2020.day05 import Run_2020_05, seat_id


class Test_2020_05:
    def setup_class(self):
        self.day = Run_2020_05()

    def test_bringup_a(self):
        assert seat_id("FBFBBFFRLR") == 357
        assert seat_id("BFFFBBFRRR") == 567
        assert seat_id("FFFBBBFRRR") == 119
        assert seat_id("BBFFBBFRLL") == 820

    def test_bringup_b(self):
        pass

    def test_regression_a(self):
        assert self.day.run_part("a") == 987

    def test_regression_b(self):
        assert self.day.run_part("b") == 603
