import pytest
from aoc2017.day03 import Run_2017_03


class Test_2017_03:
    def setup_class(self):
        self.day = Run_2017_03()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", ["1"]) == 0

    def test_bringup_a_2(self):
        assert self.day.run_part("a", ["12"]) == 3

    def test_bringup_a_3(self):
        assert self.day.run_part("a", ["23"]) == 2

    def test_bringup_a_4(self):
        assert self.day.run_part("a", ["1024"]) == 31

    def test_regression_a(self):
        assert self.day.run_part("a") == 326

    def test_regression_b(self):
        assert self.day.run_part("b") == 363010
