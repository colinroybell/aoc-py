import pytest
from aoc2025.day12 import Run_2025_12


class Test_2025_12:
    def setup_class(self):
        self.day = Run_2025_12()

    @pytest.mark.skip
    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 0

    @pytest.mark.skip
    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 0

    def test_regression_a(self):
        assert self.day.run_part("a") == 567

    @pytest.mark.skip
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
