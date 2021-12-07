import pytest
from aoc2021.day07 import Run_2021_07


class Test_2021_07:
    def setup_class(self):
        self.day = Run_2021_07()

    def test_bringup_a(self):
        assert self.day.run_part("a", ["16,1,2,0,4,2,7,1,2,14"]) == 37

    def test_bringup_b(self):
        assert self.day.run_part("b", ["16,1,2,0,4,2,7,1,2,14"]) == 168

    def test_regression_a(self):
        assert self.day.run_part("a") == 341534

    def test_regression_b(self):
        assert self.day.run_part("b") == 93397632
