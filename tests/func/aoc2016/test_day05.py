import pytest
from aoc2016.day05 import Run_2016_05


class Test_2016_05:
    def setup_class(self):
        self.day = Run_2016_05()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == "18f47a30"

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == "05ace8e3"

    def test_regression_a(self):
        assert self.day.run_part("a") == "801b56a7"

    def test_regression_b(self):
        assert self.day.run_part("b") == "424a0197"
