import pytest
from aoc2017.day17 import Run_2017_17


class Test_2017_17:
    def setup_class(self):
        self.day = Run_2017_17()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 638

    def test_bringup_b(self):
        pass

    def test_regression_a(self):
        assert self.day.run_part("a") == 355

    def test_regression_b(self):
        assert self.day.run_part("b") == 6154117
