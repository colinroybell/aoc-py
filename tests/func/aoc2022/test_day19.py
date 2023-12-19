import pytest
from aoc2022.day19 import Run_2022_19


class Test_2022_19:
    def setup_class(self):
        self.day = Run_2022_19()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 33

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 56 * 62

    def test_regression_a(self):
        assert self.day.run_part("a") == 1624

    def test_regression_b(self):
        assert self.day.run_part("b") == 12628
