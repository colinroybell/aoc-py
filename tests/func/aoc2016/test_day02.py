import pytest
from aoc2016.day02 import Run_2016_02


class Test_2016_02:
    def setup_class(self):
        self.day = Run_2016_02()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == "1985"

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == "5DB3"

    def test_regression_a(self):
        assert self.day.run_part("a") == "45973"

    def test_regression_b(self):
        assert self.day.run_part("b") == "27CA4"
