import pytest
from aoc2023.day17 import Run_2023_17


class Test_2023_17:
    def setup_class(self):
        self.day = Run_2023_17()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 102

    def test_bringup_b_1(self):
        assert self.day.run_part("b", "test1") == 94

    def test_bringup_b_2(self):
        assert self.day.run_part("b", "test2") == 71

    def test_regression_a(self):
        assert self.day.run_part("a") == 916

    @pytest.mark.xfail
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
