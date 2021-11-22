import pytest
from aoc2019.day13 import Run_2019_13


class Test_2019_13:
    def setup_class(self):
        self.day = Run_2019_13()

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
