import pytest
from aoc2022.day05 import Run_2022_05


class Test_2022_05:
    def setup_class(self):
        self.day = Run_2022_05()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == "CMZ"

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == "MCD"

    def test_regression_a(self):
        assert self.day.run_part("a") == "WSFTMRHPP"

    def test_regression_b(self):
        assert self.day.run_part("b") == "GSLCMFBRP"
