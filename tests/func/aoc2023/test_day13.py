import pytest
from aoc2023.day13 import Run_2023_13


class Test_2023_13:
    def setup_class(self):
        self.day = Run_2023_13()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 405

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 400

    def test_regression_a(self):
        assert self.day.run_part("a") == 31739

    def test_regression_b(self):
        assert self.day.run_part("b") == 31539
