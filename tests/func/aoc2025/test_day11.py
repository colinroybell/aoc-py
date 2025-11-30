import pytest
from aoc2025.day11 import Run_2025_11


class Test_2025_11:
    def setup_class(self):
        self.day = Run_2025_11()

    @pytest.mark.skip
    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 0

    @pytest.mark.skip
    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 0

    @pytest.mark.skip
    def test_regression_a(self):
        assert self.day.run_part("a") == 0

    @pytest.mark.skip
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
