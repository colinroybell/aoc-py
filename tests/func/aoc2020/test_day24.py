import pytest
from aoc2020.day24 import Run_2020_24


class Test_2020_24:
    def setup_class(self):
        self.day = Run_2020_24()

    def test_regression_a(self):
        assert self.day.run_part("a") == 488

    def test_regression_b(self):
        assert self.day.run_part("b") == 4118
