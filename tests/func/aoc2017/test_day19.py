import pytest
from aoc2017.day19 import Run_2017_19


class Test_2017_19:
    def setup_class(self):
        self.day = Run_2017_19()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == "ABCDEF"

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 38

    def test_regression_a(self):
        assert self.day.run_part("a") == "KGPTMEJVS"

    def test_regression_b(self):
        assert self.day.run_part("b") == 16328
