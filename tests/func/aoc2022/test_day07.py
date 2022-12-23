import pytest
from aoc2022.day07 import Run_2022_07


class Test_2022_07:
    def setup_class(self):
        self.day = Run_2022_07()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 95437

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 24933642

    def test_regression_a(self):
        assert self.day.run_part("a") == 1490523

    def test_regression_b(self):
        assert self.day.run_part("b") == 12390492
