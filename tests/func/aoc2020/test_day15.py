import pytest
from aoc2020.day15 import Run_2020_15


class Test_2020_15:
    def setup_class(self):
        self.day = Run_2020_15()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 436

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 175594

    def test_regression_a(self):
        assert self.day.run_part("a") == 639

    @pytest.mark.skip
    # Worker crashes sometimes?
    def test_regression_b(self):
        assert self.day.run_part("b") == 266
