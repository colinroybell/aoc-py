import pytest
from aoc2017.day02 import Run_2017_02


class Test_2017_02:
    def setup_class(self):
        self.day = Run_2017_02()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 18

    def test_bringup_b(self):
        assert self.day.run_part("b", "test2") == 9

    def test_regression_a(self):
        assert self.day.run_part("a") == 45972

    @pytest.mark.xfail
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
