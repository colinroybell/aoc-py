import pytest
from aoc2016.day02 import Run_2016_02


class Test_2016_02:
    def setup_class(self):
        self.day = Run_2016_02()

    def test_bringup_a(self):
        pass

    @pytest.mark.skip
    def test_bringup_b(self):
        pass

    @pytest.mark.xfail
    def test_regression_a(self):
        assert self.day.run_part("a") == 0

    @pytest.mark.xfail
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
