import pytest
from aoc2015.day24 import Run_2015_24


class Test_2015_24:
    def setup_class(self):
        self.day = Run_2015_24()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 99

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 44

    def test_regression_a(self):
        assert self.day.run_part("a") == 11846773891

    def test_regression_b(self):
        assert self.day.run_part("b") == 80393059
