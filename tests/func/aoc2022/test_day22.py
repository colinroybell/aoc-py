import pytest
from aoc2022.day22 import Run_2022_22


class Test_2022_22:
    def setup_class(self):
        self.day = Run_2022_22()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 6032

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 5031

    def test_regression_a(self):
        assert self.day.run_part("a") == 65368

    def test_regression_b(self):
        assert self.day.run_part("b") == 156166
