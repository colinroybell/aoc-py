import pytest
from aoc2022.day25 import Run_2022_25


class Test_2022_25:
    def setup_class(self):
        self.day = Run_2022_25()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == "2=-1=0"

    def test_bringup_b(self):
        pass

    def test_regression_a(self):
        assert self.day.run_part("a") == "20===-20-020=0001-02"

    def test_regression_b(self):
        pass
