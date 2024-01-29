import pytest
from aoc2017.day18 import Run_2017_18


class Test_2017_18:
    def setup_class(self):
        self.day = Run_2017_18()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 4

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 1

    def test_regression_a(self):
        assert self.day.run_part("a") == 2951

    @pytest.mark.xfail
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
