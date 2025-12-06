import pytest
from aoc2016.day24 import Run_2016_24


class Test_2016_24:
    def setup_class(self):
        self.day = Run_2016_24()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 14

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 20

    def test_regression_a(self):
        assert self.day.run_part("a") == 502

    def test_regression_b(self):
        assert self.day.run_part("b") == 724
