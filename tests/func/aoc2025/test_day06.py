import pytest
from aoc2025.day06 import Run_2025_06


class Test_2025_06:
    def setup_class(self):
        self.day = Run_2025_06()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 4277556

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 3263827

    def test_regression_a(self):
        assert self.day.run_part("a") == 4648618073226

    def test_regression_b(self):
        assert self.day.run_part("b") == 7329921182115
