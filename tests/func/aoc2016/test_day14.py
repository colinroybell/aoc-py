import pytest
from aoc2016.day14 import Run_2016_14


class Test_2016_14:
    def setup_class(self):
        self.day = Run_2016_14()

    def test_bringup_a(self):
        pass

    def test_bringup_b(self):
        pass

    @pytest.mark.xfail
    def test_regression_a(self):
        assert self.day.run_part("a") == 0

    @pytest.mark.xfail
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
