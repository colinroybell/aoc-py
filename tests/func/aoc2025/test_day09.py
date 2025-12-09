import pytest
from aoc2025.day09 import Run_2025_09


class Test_2025_09:
    def setup_class(self):
        self.day = Run_2025_09()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 50

    @pytest.mark.skip
    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 24

    def test_regression_a(self):
        assert self.day.run_part("a") == 4744899849

    @pytest.mark.skip
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
