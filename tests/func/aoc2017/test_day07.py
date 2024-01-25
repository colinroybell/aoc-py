import pytest
from aoc2017.day07 import Run_2017_07


class Test_2017_07:
    def setup_class(self):
        self.day = Run_2017_07()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == "tknk"

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 60

    def test_regression_a(self):
        assert self.day.run_part("a") == "svugo"

    def test_regression_b(self):
        assert self.day.run_part("b") == 1152
