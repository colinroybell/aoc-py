import pytest
from aoc2020.day25 import Run_2020_25


class Test_2020_25:
    def setup_class(self):
        self.day = Run_2020_25()

    def test_regression_a(self):
        assert self.day.run_part("a") == 4441893

    def test_regression_b(self):
        pass
