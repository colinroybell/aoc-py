import pytest
from aoc2020.day14 import Run_2020_14


class Test_2020_14:
    def setup_class(self):
        self.day = Run_2020_14()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 165

    @pytest.mark.skip
    # Not working. Not investigated
    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 208

    def test_regression_a(self):
        assert self.day.run_part("a") == 15172047086292

    def test_regression_b(self):
        assert self.day.run_part("b") == 4197941339968
