import pytest
from aoc2021.day24 import Run_2021_24


class Test_2021_24:
    def setup_class(self):
        self.day = Run_2021_24()

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
