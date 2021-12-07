import pytest
from aoc2021.day06 import Run_2021_06


class Test_2021_06:
    def setup_class(self):
        self.day = Run_2021_06()

    def test_bringup_a(self):
        assert self.day.run_part("a", ["3,4,3,1,2"], days=18) == 26
        assert self.day.run_part("a", ["3,4,3,1,2"]) == 5934

    def test_bringup_b(self):
        assert self.day.run_part("b", ["3,4,3,1,2"], days=18) == 26
        assert self.day.run_part("b", ["3,4,3,1,2"], days=80) == 5934
        assert self.day.run_part("b", ["3,4,3,1,2"]) == 26984457539

    def test_regression_a(self):
        assert self.day.run_part("a") == 350605

    def test_regression_b(self):
        assert self.day.run_part("b") == 1592778185024
