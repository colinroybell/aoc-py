import pytest
from aoc2023.day19 import Run_2023_19


class Test_2023_19:
    def setup_class(self):
        self.day = Run_2023_19()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 19114

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 167409079868000

    def test_regression_a(self):
        assert self.day.run_part("a") == 319295

    def test_regression_b(self):
        assert self.day.run_part("b") == 110807725108076
