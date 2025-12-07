import pytest
from aoc2025.day07 import Run_2025_07


class Test_2025_07:
    def setup_class(self):
        self.day = Run_2025_07()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 21

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 40

    def test_regression_a(self):
        assert self.day.run_part("a") == 1646

    @pytest.mark.skip
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
