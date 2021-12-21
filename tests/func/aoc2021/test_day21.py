import pytest
from aoc2021.day21 import Run_2021_21


class Test_2021_21:
    def setup_class(self):
        self.day = Run_2021_21()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 739785

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 444356092776315

    @pytest.mark.xfail
    def test_regression_a(self):
        assert self.day.run_part("a") == 598416

    @pytest.mark.xfail
    def test_regression_b(self):
        assert self.day.run_part("b") == 27674034218179
