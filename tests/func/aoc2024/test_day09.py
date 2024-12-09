import pytest
from aoc2024.day09 import Run_2024_09


class Test_2024_09:
    def setup_class(self):
        self.day = Run_2024_09()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 1928

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 2858

    def test_regression_a(self):
        assert self.day.run_part("a") == 6607511583593

    def test_regression_b(self):
        assert self.day.run_part("b") == 6636608781232
