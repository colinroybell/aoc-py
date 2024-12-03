import pytest
from aoc2016.day06 import Run_2016_06


class Test_2016_06:
    def setup_class(self):
        self.day = Run_2016_06()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == "easter"

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == "advent"

    def test_regression_a(self):
        assert self.day.run_part("a") == "gyvwpxaz"

    def test_regression_b(self):
        assert self.day.run_part("b") == "jucfoary"
