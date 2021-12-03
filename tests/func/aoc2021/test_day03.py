import pytest
from aoc2021.day03 import Run_2021_03


class Test_2021_03:
    def setup_class(self):
        self.day = Run_2021_03()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 198

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 230

    def test_regression_a(self):
        assert self.day.run_part("a") == 3882564

    @pytest.mark.xfail
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
