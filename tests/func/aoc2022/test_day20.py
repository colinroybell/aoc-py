import pytest
from aoc2022.day20 import Run_2022_20


class Test_2022_20:
    def setup_class(self):
        self.day = Run_2022_20()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 3

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 1623178306

    def test_regression_a(self):
        # assert self.day.run_part("a") == 5498
        pass

    @pytest.mark.xfail
    def test_regression_b(self):
        # assert self.day.run_part("b") == 0
        pass
