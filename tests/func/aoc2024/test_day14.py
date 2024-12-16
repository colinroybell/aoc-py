import pytest
from aoc2024.day14 import Run_2024_14


class Test_2024_14:
    def setup_class(self):
        self.day = Run_2024_14()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1", width=11, height=7) == 12

    @pytest.mark.skip
    def test_bringup_b(self):
        pass

    def test_regression_a(self):
        assert self.day.run_part("a") == 231221760

    @pytest.mark.skip
    def test_regression_b(self):
        assert self.day.run_part("b") == 6771
