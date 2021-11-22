import pytest
from aoc2015.day03 import Run_2015_03

@pytest.mark.bringup
class Test_2015_03:
    def setup_class(self):
        self.day = Run_2015_03()

    def test_a(self):
        assert self.day.run_part("a",[">"]) == 2
        assert self.day.run_part("a",["^>v<"]) == 4
        assert self.day.run_part("a",["^v^v^v^v^v"]) == 2

    def test_b(self):
        assert self.day.run_part("b",["^v"]) == 3
        assert self.day.run_part("b",["^>v<"]) == 3
        assert self.day.run_part("b",["^v^v^v^v^v"]) == 11

    def test_regression_a(self):
        assert self.day.run_part("a") == 2081

    def test_regression_b(self):
        assert self.day.run_part("b") == 2341
