import pytest
from aoc2025.day08 import Run_2025_08


class Test_2025_08:
    def setup_class(self):
        self.day = Run_2025_08()

    def test_bringup_a(self):
        # assert self.day.run_part("a", "test1",junctions=1) == 2
        # assert self.day.run_part("a", "test1",junctions=3) == 6
        assert self.day.run_part("a", "test1", junctions=4) == 6
        assert self.day.run_part("a", "test1", junctions=10) == 40

    @pytest.mark.skip
    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 0

    def test_regression_a(self):
        assert self.day.run_part("a") == 69192

    @pytest.mark.skip
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
