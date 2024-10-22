import pytest
from aoc2015.day11 import Run_2015_11


class Test_2015_11:
    def setup_class(self):
        self.day = Run_2015_11()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", ["abcdefgh"]) == "abcdffaa"

    def test_bringup_a_2(self):
        assert self.day.run_part("a", ["ghijklmn"]) == "ghjaabcc"

    def test_regression_a(self):
        assert self.day.run_part("a") == "hepxxyzz"

    def test_regression_b(self):
        assert self.day.run_part("b") == "heqaabcc"
