import pytest
from aoc2015.day25 import Run_2015_25, locate, lookup


class Test_2015_25:
    def setup_class(self):
        self.day = Run_2015_25()

    def test_bringup_a_1(self):
        assert locate(4, 2) == 12
        assert locate(1, 5) == 15

    def test_bringup_a_2(self):
        assert lookup(1, 1) == 20151125
        assert lookup(1, 6) == 33511524
        assert lookup(6, 1) == 33071741
        assert lookup(6, 6) == 27995004

    def test_regression_a(self):
        assert self.day.run_part("a") == 2650453

    @pytest.mark.xfail
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
