import pytest
from aoc2023.day24 import Run_2023_24


class Test_2023_24:
    def setup_class(self):
        self.day = Run_2023_24()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1", test_min=7, test_max=27) == 2

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 47

    def test_regression_a(self):
        assert self.day.run_part("a") == 25810

    def test_regression_b(self):
        assert self.day.run_part("b") == 652666650475950
